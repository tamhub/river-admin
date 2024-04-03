<template>
  <div v-resize="onResize" class="w-full bg-[#E9E9E9] rounded-[20px] relative" style="height: calc(100vh - 300px);">
    <span class="absolute top-0 left-0 px-6 py-4 text-[#A0A2A7]">Diagram</span>
    <v-card-text>
      <v-container fluid>
        <v-row justify="center" align="center">
          <v-col id="svg-container" justify="center" align="center">
            <svg id="svg" width="650" height="270" class="">
              <defs>
                <filter id="dropshadow" height="130%">
                  <feGaussianBlur in="SourceAlpha" stdDeviation="3" /> <!-- Blur amount -->
                  <feOffset dx="2" dy="2" result="offsetblur" /> <!-- Shadow offset -->
                  <feFlood flood-color="#5E45FF33" result="color" /> <!-- Change 'red' to your desired shadow color -->
                  <feComposite in2="offsetblur" operator="in" result="shadow" />
                  <feComponentTransfer>
                    <feFuncA type="linear" slope="0.1" /> <!-- Shadow transparency -->
                  </feComponentTransfer>
                  <feMerge>
                    <feMergeNode in="shadow" /> <!-- This contains the colored shadow -->
                    <feMergeNode in="SourceGraphic" /> <!-- This contains the original element -->
                  </feMerge>
                </filter>
                <marker id="start-marker" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6"
                  orient="auto-start-reverse">
                  <circle cx="5" cy="5" r="3" fill="transparent" />
                </marker>
                <marker id="end-marker" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6"
                  orient="auto">
                  <circle cx="5" cy="5" r="3" fill="transparent" />
                </marker>
              </defs>
            </svg>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
  </div>
</template>

<script>
import * as d3 from "d3";
import d3Tip from "d3-tip";
import dagreD3 from "dagre-d3";

d3.tip = d3Tip;

export default {
  name: "WorkflowIllustration",
  props: ["states", "transitions", "editable", "state_class_mapping"],
  computed: {},
  data: () => ({
    svg: null,
    initialized: false,
    selected_transition_id: null,
    windowSize: {
      x: 0,
      y: 0
    }
  }),
  mounted() {
    this._initialize();
  },
  watch: {
    state_class_mapping: {
      deep: true,
      handler(val) {
        this._setClasses();
      }
    },
    states(val) {
      this._renderSketch();
    },
    transitions(val) {
      this._renderSketch();
    }
  },
  methods: {
    onResize() {
      if (this.svg) {
        if (Math.abs(this.windowSize.x - window.innerWidth) > 50) {
          this.windowSize = { x: window.innerWidth, y: window.innerHeight };
          var containerWidth = d3
            .select("#svg-container")
            .node()
            .getBoundingClientRect().width;

          d3.select("svg").attr("width", containerWidth - 24);
          document.getElementById('svg').attributes.width.value = containerWidth - 24;
          this._reCenterSketch();
        }
      }
    },
    _getChilds(stateId) {
      return this.transitions
        .filter(transition => transition.source_state_id == stateId)
        .map(transition => this._get_state_by_id(transition.destination_state_id));
    },
    _initialize() {
      if ((this.states && this.states.length > 0) || (this.transitions && this.transitions.length > 0)) {
        var el = d3.select(this.$el);
        this.svg = el.select("svg");
        this.svgGroup = this.svg.append("g");

        this.graph = new dagreD3.graphlib.Graph().setGraph({}).setDefaultEdgeLabel(function () {
          return {};
        });

        this._renderSketch();
        this.onResize();
        this._reCenterSketch();
        this.initialized = true;
      }
    },

    _createNode(state, index) {
      this.graph.setNode(state.id, {
        label: state.label,
        class: "node-default",
        id: `state_${state.id}`,

      });
    },

    _createEdge(transition) {
      this.graph.setEdge(transition.source_state_id, transition.destination_state_id, {
        id: `transition_${transition.id}`,
        label: "  ←",
        curve: d3.curveBasis,
      });
    },

    _destroySketchComponents() {
      var g = this.graph;
      this.graph.nodes().forEach(function (v) {
        g.removeNode(v);
      });

      this.graph.edges().forEach(function (v) {
        g.removeEdge(v);
      });

      d3.selectAll(".clickable-edge").remove();
    },
    _renderSketch() {
      if (this.states.length > 0 || this.transitions.length > 0) {
        this._destroySketchComponents();

        var that = this;
        this.states.forEach((state, index) => {
          that._createNode(state, index);
        });

        this.transitions.forEach(transition => {
          that._createEdge(transition);
        });

        this._roundNodeCorners();

        var render = new dagreD3.render();
        var el = d3.select(this.$el);
        var inner = el.select("svg g");
        render(inner, this.graph);
        inner.selectAll("g.node rect").attr("rx", "20").attr("ry", "20");



        this._reCenterSketch();
        if (this.editable) {
          this._setNodeOnclicks();
        }
        this._setEdgeLabelDefaultClass();
        this._setEdgeOnclicks();
        this._setClasses();
        this._setup_tooltips(inner);
      }
    },
    _setNodeOnclicks() {
      var that = this;
      this.states.forEach(state => {
        d3.select(`g#state_${state.id} rect`).on("click", function () {
          d3.selectAll(`g.node`).classed("selected", false);
          d3.select(`g#state_${state.id}`).classed("selected", true);

          // Remove "border" from all nodes
          d3.selectAll(`g.node rect`).style("filter", "");;

          // Add "border" to the clicked node
          d3.select(this).style("filter", "url(#dropshadow)");;


          that.$emit("on-state-clicked", that._get_state_by_id(state.id));
        });
      });
    },
    _setEdgeLabelDefaultClass() {
      d3.selectAll(`g.edgeLabels > g.edgeLabel`).classed("edge-label-UNSELECTED ", true);
    },
    _setEdgeOnclicks() {
      var that = this;
      var allEdgeG = d3
        .select("g.edgePaths")
        .selectAll("g.edgePath")
        .nodes();

      this.transitions.forEach((transition, index) => {
        var edge_container = d3.select(`g#transition_${transition.id}`);
        edge_container.attr("index", index);
        edge_container
          .append("path")
          .attr("d", edge_container.select("path").attr("d"))
          .classed("clickable-edge", true)
          .on("click", function () {
            if (transition) {
              that._unselectEdge();
              that.selected_transition_id = transition.id;
              that._selectEdge();
            }
          });
      });
    },
    _setClasses() {
      var that = this;
      this.states.forEach(state => {
        if (that.state_class_mapping && that.state_class_mapping[state.id]) {
          if (that.state_class_mapping[state.id].rect) {
            Object.keys(that.state_class_mapping[state.id].rect).forEach(style => {
              d3.select(`g#state_${state.id} rect`).style(style, that.state_class_mapping[state.id].rect[style])
              // d3.select(`g#state_${state.id}`).classed("selected", true);
            }
            );
          }
          if (that.state_class_mapping[state.id].label) {
            Object.keys(that.state_class_mapping[state.id].label).forEach(style =>
              d3.select(`g#state_${state.id} g.label`).style(style, that.state_class_mapping[state.id].label[style])
            );
          }
        }
      });
    },

    _setup_tooltips(inner) {
      var that = this;
      var tip = d3
        .tip()
        .attr("class", "d3-tip")
        .html(function (d) {
          var state = that.states.find(state => state.id == d);
          if (state) {
            var label_html = `<div class="label-tooltip"><strong>${state.label}</strong></div>`;
            var description_html = "";

            if (state.description) {
              description_html = `<div class="description-tooltip">${state.description}</div>`;
            } else {
              description_html = `<div class="no-description-tooltip">No description found</div>`;
            }
          }
          return `<div>${description_html}</div>`;
        });


      var originalShow = tip.show;
      tip.show = function () {
        var targetElement = d3.event.target;
        var bbox = targetElement.getBoundingClientRect();
        var offsetWidth = bbox.width;
        tip.offset([-5, offsetWidth + 10]);
        originalShow.apply(this, arguments);
      };


      this.svg.call(tip);

      inner
        .selectAll("g.node")
        .on("mouseover", tip.show)
        .on("mouseout", tip.hide);
    },
    _getTransitionBy(sourceState, targetState) {
      return this.transitions.find(transition => transition.source_state_id == sourceState.id && transition.destination_state_id == targetState.id);
    },
    _selectEdge() {
      if (this.selected_transition_id) {
        var edge_elem = d3.select(`g#transition_${this.selected_transition_id}`);
        edge_elem.classed("edge-SELECTED", true).classed("edge-UNSELECTED", false);

        var index = new Number(edge_elem.attr("index"));
        var edge_label_elem = d3.selectAll(`g.edgeLabels > g.edgeLabel`).nodes()[index];
        d3.select(edge_label_elem)
          .classed("edge-label-SELECTED", true)
          .classed("edge-label-UNSELECTED", false);

        this.$emit("on-transition-selected", this.selected_transition_id);
      }
    },
    _unselectEdge() {
      if (this.selected_transition_id) {
        var edge_elem = d3.select(`g#transition_${this.selected_transition_id}`);
        edge_elem.classed("edge-SELECTED", false).classed("edge-UNSELECTED", true);

        var index = new Number(edge_elem.attr("index"));
        var edge_label_elem = d3.selectAll(`g.edgeLabels > g.edgeLabel`).nodes()[index];
        d3.select(edge_label_elem)
          .classed("edge-label-SELECTED", false)
          .classed("edge-label-UNSELECTED", true);

        this.$emit("on-transition-unselected", this.selected_transition_id);
      }
    },
    _reCenterSketch() {
      var xCenterOffset = (this.svg.attr("width") - this.graph.graph().width) / 2;
      this.svgGroup.attr("transform", "translate(" + xCenterOffset + ", 20)");
      this.svg.attr("height", this.graph.graph().height + 40);
    },
    _roundNodeCorners() {
      var g = this.graph;
      this.graph.nodes().forEach(function (v) {
        var node = g.node(v);
        node.rx = node.ry = 5;
      });
    },

    _get_state_by_id(state_id) {
      return this.states.find(state => state.id == state_id);
    },

    _get_transition_by_id(transition_id) {
      return this.transitions.find(transition => transition.id == transition_id);
    }
  }
};
</script>


<style>
g.node-default {
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  user-select: none;
}

g.node-default>rect {
  fill: #dddd;
  stroke: black;
  stroke-width: 0.3px;
  -webkit-filter: drop-shadow(0px 0px 10px 0px #0000000A);
  filter: drop-shadow(0px 0px 10px 0px #0000000A);
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

g.node-default>g.label {
  /* stroke: black !important; */
  stroke-width: 0.3px !important;
  pointer-events: none;
}

g.node-default.selected>rect {
  stroke: #5E45FF !important;
  box-shadow: 0 0 0 2px #5E45FF;

}

g.edge-SELECTED>rect {
  stroke: #5E45FF !important;
  stroke-width: 2.5px !important;
}

g.edge-SELECTED>path.path {
  stroke: #5E45FF !important;
  stroke-width: 1.5;
}

g.edge-SELECTED>defs * {
  stroke: #5E45FF !important;

  fill: #5E45FF !important;
  stroke-width: 1.5;
}

g.edge-UNSELECTED>path.path {
  stroke: #000 !important;
  stroke-width: 1.5px;
}

g.edge-label-SELECTED tspan {
  stroke: #5E45FF !important;
  stroke-width: 1.5;
}

g.edge-UNSELECTED>path {
  fill: #dddd;
}

g.edge-label-UNSELECTED {
  display: none;
}

.clickable-edge {
  stroke-width: 15px !important;
  stroke-miterlimit: 0 !important;
  opacity: 0 !important;
}

text {
  font-weight: 300;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
}

.edgePath path {
  stroke: #333;
  stroke-width: 1.5px;
}

.md-card {
  padding: 15px;
}

.md-layout {
  padding-left: 25px;
  padding-right: 25px;
}

.shadow>* {


  /* Similar syntax to box-shadow */
}

.d3-tip {
  line-height: 1;
  font-weight: bold;
  padding: 12px;
  background: white;
  color: #fff;
  border-radius: 16px 16px 16px 0px !important;
  box-shadow: 0px 8px 16px 0px #0000000A;
  overflow: hidden;

}

.label-tooltip {
  text-align: center;
  color: lightblue;
  margin-bottom: 10px;
}

.description-tooltip {
  text-align: center;
  max-width: 400px;
  font-size: 14px;
}

.no-description-tooltip {
  text-align: center;
  max-width: 400px;
  font-size: 14px;
  color: #A0A2A7;
}
</style>
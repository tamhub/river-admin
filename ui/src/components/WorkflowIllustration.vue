<template>
  <div v-resize="onResize"
    class="w-full bg-[#E9E9E9] rounded-[20px] relative overflow-hidden cursor-move select-none z-0"
    style="height: calc(100vh - 300px);" @mousedown="startDrag" @mouseup="stopDrag" @wheel="handleScroll">
    <span class="absolute top-0 left-0 px-6 py-4 rounded-md m-1 text-[#A0A2A7] bg-[#E9E9E9] z-10">Diagram</span>
    <v-card-text>
      <v-container fluid>
        <v-row justify="center" align="center">
          <v-col ref="draggableContainer" class="relative" id="svg-container" justify="center" align="center"
            style="top: 0px; left: 0px;"> <svg id="svg" width="650" height="270" class="">
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
    <v-dialog v-if="deleteDialog" v-model="deleteDialog" max-width="581">
      <v-card :class="{ 'custom-dialoge': !canDelete }">
        <v-card-title class="headline flex flex-col gap-[17px]">
          <svg width="133" height="132" viewBox="0 0 133 132" fill="none" class="m-auto"
            xmlns="http://www.w3.org/2000/svg">
            <path opacity="0.1"
              d="M11.5 60C11.5 90 44.8056 126 66 126C87.1944 126 120.5 90 120.5 60V42C120.5 33 114.444 24 102.333 18C102.333 18 81.1389 6 66 6C50.8611 6 29.6667 18 29.6667 18C17.5556 24 11.5 33 11.5 42V60Z"
              fill="#E33554" />
            <path opacity="0.2"
              d="M13.5 60.2C13.5 89.2 45.5833 124 66 124C86.4167 124 118.5 89.2 118.5 60.2V42.8C118.5 34.1 112.667 25.4 101 19.6C101 19.6 80.5833 8 66 8C51.4167 8 31 19.6 31 19.6C19.3333 25.4 13.5 34.1 13.5 42.8V60.2Z"
              fill="#E33554" />
            <path opacity="0.3"
              d="M16.5 60.5C16.5 88 46.75 121 66 121C85.25 121 115.5 88 115.5 60.5V44C115.5 35.75 110 27.5 99 22C99 22 79.75 11 66 11C52.25 11 33 22 33 22C22 27.5 16.5 35.75 16.5 44V60.5Z"
              fill="#E33554" />
            <path d="M66.4805 47.8335V67.8335" stroke="#E33554" stroke-width="4.5" stroke-linecap="round"
              stroke-linejoin="round" />
            <path d="M66.4805 87.8335H66.5273" stroke="#E33554" stroke-width="4.5" stroke-linecap="round"
              stroke-linejoin="round" />
          </svg>
          <span class="font-bold text-[40px] text-[#E33554]">
            {{ "State Deletion" }}
          </span>
          <p class="text-center text-xl text-[#121722] break-normal mb-0">
            {{

    "Are you sure you want to remove this state?"
  }}
          </p>
          <v-card-actions class="flex gap-[17px] items-center justify-start">
            <div
              class="flex items-center gap-2 bg-transparent text-[#5E45FF] border-[#5E45FF] border  p-4 rounded-[64px] w-[200px] ms-auto cursor-pointer"
              @click="deleteDialog = false">
              <span class=" font-bold text-base flex-1 text-center">No, keep</span>
            </div>

            <div class="flex items-center gap-2 bg-[#FFDFDF] p-4 rounded-[64px] w-[200px] ms-auto cursor-pointer"
              @click="deleteState()">
              <svg width="16" height="17" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2 4.5H3.33333H14" stroke="#E33554" stroke-linecap="round" stroke-linejoin="round" />
                <path
                  d="M5.33325 4.50016V3.16683C5.33325 2.81321 5.47373 2.47407 5.72378 2.22402C5.97383 1.97397 6.31296 1.8335 6.66659 1.8335H9.33325C9.68687 1.8335 10.026 1.97397 10.2761 2.22402C10.5261 2.47407 10.6666 2.81321 10.6666 3.16683V4.50016M12.6666 4.50016V13.8335C12.6666 14.1871 12.5261 14.5263 12.2761 14.7763C12.026 15.0264 11.6869 15.1668 11.3333 15.1668H4.66659C4.31296 15.1668 3.97382 15.0264 3.72378 14.7763C3.47373 14.5263 3.33325 14.1871 3.33325 13.8335V4.50016H12.6666Z"
                  stroke="#E33554" stroke-linecap="round" stroke-linejoin="round" />
              </svg>

              <!-- <v-icon
                    class="mr-1"
                    color="warning"
                    @click="showDeletingDialog(item)"
                    :disabled="!has_delete_state_permission"
                    >mdi-delete</v-icon
                  > -->
              <span class="text-[#FF0F0F] font-bold text-base flex-1 text-center">Yes, delete</span>
            </div>
          </v-card-actions>
        </v-card-title>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { emit_success } from "@/helpers/event_bus";
import http from "@/helpers/http";
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
    },
    dragging: false,
    resizing: false,
    initialX: 0,
    initialY: 0,
    deleteDialog: false,
    canDelete: false,
    deletingState: null,
    stateToBeDeletedId: null

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
    startDrag(event) {
      this.dragging = true;
      this.initialX = event.clientX;
      this.initialY = event.clientY;

      const rect = this.$refs.draggableContainer.getBoundingClientRect();
      // Initialize left and top if they are not set
      if (!this.$refs.draggableContainer.style.left) {
        this.$refs.draggableContainer.style.left = rect.left + 'px';
      }
      if (!this.$refs.draggableContainer.style.top) {
        this.$refs.draggableContainer.style.top = rect.top + 'px';
      }

      document.addEventListener('mousemove', this.drag);
      document.addEventListener('mouseup', this.stopDrag);
    },
    drag(event) {
      if (!this.dragging) return;
      const deltaX = event.clientX - this.initialX;
      const deltaY = event.clientY - this.initialY;

      // Check if the drag distance exceeds the minimum threshold
      const minDragDistance = 1; // Adjust this value as needed
      if (Math.abs(deltaX) > minDragDistance || Math.abs(deltaY) > minDragDistance) {
        // Update left and top based on the delta
        let newLeft = parseInt(this.$refs.draggableContainer.style.left) + deltaX;
        let newTop = parseInt(this.$refs.draggableContainer.style.top) + deltaY;

        this.$refs.draggableContainer.style.left = newLeft + 'px';
        this.$refs.draggableContainer.style.top = newTop + 'px';

        // Update initial positions for the next move
        this.initialX = event.clientX;
        this.initialY = event.clientY;
      }
    },
    stopDrag() {
      this.dragging = false;
      document.removeEventListener('mousemove', this.drag);
      document.removeEventListener('mouseup', this.stopDrag);
    },
    handleScroll(event) {
      if (event.ctrlKey) {
        event.preventDefault(); // Prevent the default scroll behavior
        const scaleAmount = 0.1;
        const container = this.$refs.draggableContainer;
        let scale = Number(container.getAttribute('data-scale')) || 1;
        if (event.deltaY < 0) {
          scale += scaleAmount; // Zoom in
        } else {
          scale -= scaleAmount; // Zoom out
        }
        // Ensure scale does not go below a minimum value, e.g., 0.1
        scale = Math.max(scale, 0.1);
        container.style.transform = `scale(${scale})`;
        container.setAttribute('data-scale', scale); // Store the current scale
      }
    },
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

        inner.selectAll("g.node").each(function (nodeId) {
          console.log(that.editable);
          if (that.editable) {


            let nodeElement = d3.select(this);
            let nodeWidth = nodeElement.node().getBBox().width;
            let nodeHeight = nodeElement.node().getBBox().height;

            let deleteButton = nodeElement.append("g")
              .attr("class", "delete-button")
              .attr("transform", `translate(${(nodeWidth / 2) - 10}, -20)`) // Adjust the position relative to the node
              .on("click", () => {
                that._deleteState(nodeId);
              });

            deleteButton.append("circle")
              .attr("cx", 10)
              .attr("cy", 10)
              .attr("r", 10)
              .attr("fill", "#b53737");

            deleteButton.append("text")
              .attr("x", 10)
              .attr("y", 15)
              .attr("text-anchor", "middle")
              .attr("fill", "white")
              .text("-");
          }
        });

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
              d3.select(`g#state_${state.id} rect`).style(style, that.state_class_mapping[state.id].rect[style]);
              d3.select(`g#state_${state.id}`).classed(that.state_class_mapping[state.id].class, true);
            }
            );
          }
          if (that.state_class_mapping[state.id].label) {
            Object.keys(that.state_class_mapping[state.id].label).forEach(style => {
              d3.select(`g#state_${state.id} g.label`).style(style, `${that.state_class_mapping[state.id].label[style]}`).classed(that.state_class_mapping[state.id].class, true);

            }
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
        .on("mouseover", function (d) {
          if (!d3.event.target.closest(".delete-button")) {
            tip.show.apply(this, arguments);
          }
        })
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
    },
    _deleteState(stateId) {
      this.stateToBeDeletedId = stateId;
      this.deleteDialog = true;


    },
    deleteState() {
      http.delete(`/state/delete/${this.stateToBeDeletedId}/`, () => {
        // this.fetchStates();
        this.$emit("refetch");
        this.deleteDialog = false;
        emit_success(`State is deleted`);
      });
    }
  }
};
</script>


<style>
g.node-default {
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  user-select: none;
  position: relative;
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

g.node-default>g.label.current {
  stroke: #5E45FF !important;
  fill: #5E45FF !important;
  stroke-width: 0.3px !important;
  pointer-events: none;
}

g.node-default.current>rect {
  stroke: #5E45FF !important;
  box-shadow: 0 0 0 2px #5E45FF;
}

g.node-default>g.label.done {
  stroke: #4caf50 !important;
  fill: #4caf50 !important;
  stroke-width: 0.3px !important;
  pointer-events: none;
}

g.node-default.done>rect {
  stroke: #4caf50 !important;
  box-shadow: 0 0 0 2px #4caf50;
}

g.node-default>g.label.cancelled {
  stroke: #4caf50 !important;
  fill: #4caf50 !important;
  stroke-width: 0.3px !important;
  pointer-events: none;
}

g.node-default.cancelled>rect {
  stroke: #4caf50 !important;
  box-shadow: 0 0 0 2px #4caf50;
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
  cursor: pointer;
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

g.node-default .delete-button {
  display: none;
  cursor: pointer;
  pointer-events: all;
  position: absolute;
  top: -10px;
  right: -10px;
}

g.node-default:hover .delete-button {
  display: block;
}
</style>
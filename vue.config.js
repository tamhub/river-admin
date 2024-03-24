module.exports = {
  // options...
  publicPath: "",
  outputDir: __dirname + "/river_admin/templates/",
  assetsDir: "../static/",
  devServer: {
    proxy: "http://127.0.0.1:8000/",
  },

  configureWebpack: {
    resolve: {
      alias: {
        "@": __dirname + "/ui/src/",
      },
    },
    entry: {
      app: __dirname + "/ui/src/main.js",
    },
  },
  chainWebpack: (config) => {
    // Clear existing SVG loader
    const svgRule = config.module.rule("svg");
    svgRule.uses.clear();

    // Use vue-svg-loader for SVG files
    svgRule.use("vue-svg-loader").loader("vue-svg-loader");
  },
};

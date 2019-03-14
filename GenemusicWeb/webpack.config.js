const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    "mode": "development",
    "entry": ["./src/app.js"],
    "output": {
        "path": __dirname+'/dist',
        "filename": "[name].[hash:8].js"
    },
    "module": {
        "rules": [
            {
                "test": /\.js$/,
                "exclude": /node_modules/,
                "use": {
                    "loader": "babel-loader",
                    "options": {
                        "presets": [
                            "@babel/preset-env"
                        ],
                        "plugins": ["@babel/plugin-proposal-class-properties"]
                    }
                },
            },
            {
                test: /\.css$/,
                use:  [  'style-loader', MiniCssExtractPlugin.loader, 'css-loader']
            }
        ]
    },
    "plugins": [
        new MiniCssExtractPlugin({
            filename: 'index.[hash:8].css',
        }),
        new HtmlWebpackPlugin({
            title: 'Custom template',
            // Load a custom template (lodash by default)
            template: 'src/index.html'
        }),
    ]
}
module.exports = {
    "mode": "development",
    "entry": "src/app.js",
    "output": {
        "path": __dirname+'/dist',
        "filename": "[name].[chunkhash:8].js"
    },
    "module": {
        "rules": [
            {
                "enforce": "pre",
                "test": /\.(js|jsx)$/,
                "exclude": /node_modules/,
                "use": "eslint-loader"
            },
            {
                "test": /\.js$/,
                "exclude": /node_modules/,
                "use": {
                    "loader": "babel-loader",
                    "options": {
                        "presets": [
                            "env"
                        ]
                    }
                }
            }
        ]
    }
}
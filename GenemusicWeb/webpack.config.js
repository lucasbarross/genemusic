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
                        ]
                    }
                }
            }
        ]
    }
}
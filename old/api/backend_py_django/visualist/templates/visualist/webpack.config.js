var ExtractTextPlugin = require('extract-text-webpack-plugin')
var autoprefixer = require('autoprefixer')
var webpack = require('webpack')

// all UI is handled by the visualist app
var project_dir = __dirname + '/django_project/visualist'

var config = {
    cache: false, // turn on if "$export" bug occurs
    output: {
        path: project_dir,
        filename: '[name]'
    },
    context: project_dir,
    entry: {
        // synchronous styles
        './static/visualist/bundle.css': [
            './templates/visualist/base.scss',
            './templates/visualist/_header/_header.scss',
            './templates/visualist/_footer/_footer.scss',
        ],

        // synchronous header and footer logic
        './static/visualist/bundle.js': [
            // './templates/visualist/base.js',
            './templates/visualist/_header/_header.js',
            // './templates/visualist/_footer/_footer.js',
        ],

        // page bundles; one set per view
        './static/visualist/home.js':        './templates/visualist/home/home.js',
        './static/visualist/home.css':       './templates/visualist/home/home.scss',
        './static/visualist/search.js':      './templates/visualist/search/search.js',
        './static/visualist/search.css':     './templates/visualist/search/search.scss',
        './static/visualist/event.js':       './templates/visualist/event/event.js',
        './static/visualist/event.css':      './templates/visualist/event/event.scss',
        './static/visualist/events.js':  './templates/visualist/events/events.js',
        './static/visualist/events.css': './templates/visualist/events/events.scss',
    },
    devtool: 'source-map',
    module: {
        // preLoaders: [],
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel',
                exclude: /node_modules/
            },
            {
                test: /\.vue$/,
                loader: 'vue',
                options: {
                    loaders: {
                        'js': 'babel',
                        'scss': 'vue-style-loader!style!css!postcss!sass',
                        'sass': 'vue-style-loader!style!css!postcss!sass?indentedSyntax'
                    }
                }
            },
            {
                test: /\.scss$/,
                loader: "style!css!postcss!sass",
                exclude: /templates/
            },
            {
                test: /templates.*\.scss$/,
                loader: ExtractTextPlugin.extract("style", "css!postcss!sass")
            },
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.common.js'
        }
    },
    plugins: [
        new ExtractTextPlugin('[name]')
    ],
    postcss: [
        autoprefixer({
            browsers: "last 2 versions"
        })
    ]
}

module.exports = config

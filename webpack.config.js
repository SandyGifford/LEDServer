const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
	mode: "development",
	entry: {
		"app": "./src/index.tsx",
	},
	output: {
		path: path.resolve(process.cwd(), "dist/build"),
		filename: "js/[name].js",
	},
	module: {
		rules: [
			{ test: /\.tsx?$/, use: ["ts-loader"] },
			{
				test: /\.((s[ac])|(c))ss$/i,
				use: [
					{
						loader: MiniCssExtractPlugin.loader,
					},
					{
						loader:"css-loader",
						options: {
							url: false,
						},
					},
					"sass-loader",
				],
			},
			{ test: /\.pug$/, use: [{
				loader: "pug3-loader",
			}] },
		],
	},
	resolve: {
		extensions: [".js", ".jsx", ".ts", ".tsx", ".scss", ".css"],
	},
	devtool: "source-map",
	plugins: [
		new MiniCssExtractPlugin({
			filename: "css/[name].css",
		}),
		new HtmlWebpackPlugin({
			template: "src/pug/index.pug",
			filename: "index.html",
		}),
	],
};

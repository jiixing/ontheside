var React = require('react');
var Router = require('react-router');
var App = require('./components/App.jsx');
var Home = require('./components/Home.jsx');

var Route = Router.Route;
var DefaultRoute = Router.DefaultRoute;

var routes = (
  <Route name="app" path="/" handler={App}>
    <DefaultRoute name="home" handler={Home}/>
  </Route>
)

Router.run(routes, function(Handler) {
  React.render(<Handler />, document.getElementById('app'));
});

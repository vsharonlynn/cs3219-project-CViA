import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('jobs');
  this.route('job', {
    path: '/job/:job_id'
  });
  this.route('profile');
  this.route('submission');
  this.route('signup');
});

export default Router;

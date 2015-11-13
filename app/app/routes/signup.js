import Ember from 'ember';

export default Ember.Route.extend({
  session: Ember.inject.service('session'),
  beforeModel() {
    if (this.get('session').session.isAuthenticated) {
      this.transitionTo('profile');
    }
  },
  actions: {
    toJobs() {
      this.transitionTo('jobs');
    }
  }
});

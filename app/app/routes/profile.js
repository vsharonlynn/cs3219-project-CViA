import Ember from 'ember';

export default Ember.Route.extend({
  session: Ember.inject.service('session'),
  beforeModel() {
    if (!this.get('session').session.isAuthenticated) {
      this.transitionTo('signup');
    }
  },
  model() {
    return {
      user: this.store.findRecord('user', 'current'),
      resumes: this.store.findAll('resume'),
      jobs: this.store.findAll('my-job')
    };
  }
});

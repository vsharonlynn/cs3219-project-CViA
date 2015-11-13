import Ember from 'ember';

export default Ember.Route.extend({
  model() {
    return {
      user: this.store.findRecord('user', 'current'),
      jobs: this.store.findAll('job'),
      resumes: this.store.findAll('resume')
    };
  }
});

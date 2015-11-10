import Ember from 'ember';

export default Ember.Route.extend({
  model() {
    return {
      jobs: this.store.findAll('job')
    };
  }
});

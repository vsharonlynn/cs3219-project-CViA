import Ember from 'ember';

export default Ember.Route.extend({
  model() {
    return {
      user: this.store.findRecord('user', 'current'),
    };
  }
});

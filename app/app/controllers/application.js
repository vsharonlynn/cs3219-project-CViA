import Ember from 'ember';

export default Ember.Controller.extend({
  model() {
    return {
      user: this.store.findRecord('user', 'current')
    }
  }
});

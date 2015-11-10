import Ember from 'ember';

export default Ember.Component.extend({
  session: Ember.inject.service('session'),
  store: Ember.inject.service(),

  model() {
    return {
      user: this.store.findRecord('user', 'current')
    };
  },

  actions: {
    login() {
      const email = this.get('email');
      const password = this.get('password');
      this.get('session').authenticate('authenticator:django', {
        username:email, email, password
      });
    }
  }
});

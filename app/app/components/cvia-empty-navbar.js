import Ember from 'ember';

export default Ember.Component.extend({
  session: Ember.inject.service('session'),

  actions: {
    login() {
      const username = this.get('username');
      const password = this.get('password');
      this.get('session').authenticate('authenticator:django', {
        username, password
      });
    }
  }
});

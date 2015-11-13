import Ember from 'ember';

export default Ember.Component.extend({
  session: Ember.inject.service('session'),
  actions: {
    login() {
      const email = this.get('email');
      const password = this.get('password');
      this.get('session').authenticate('authenticator:django', {
        username:email, email, password
      }).then(success => {
        window.location.reload();
      }).catch(err => {
      });
    }
  }
});

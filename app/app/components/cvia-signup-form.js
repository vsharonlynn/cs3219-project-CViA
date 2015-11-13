import Ember from 'ember';
import $ from 'jquery';

export default Ember.Component.extend({
  tagName: '',
  session: Ember.inject.service('session'),
  actions: {
    toJobs() {
      this.sendAction('action');
      return true;
    },
    signup() {
      const first_name = this.get('first_name');
      const last_name = this.get('last_name');
      const email = this.get('email');
      const password1 = this.get('password1');
      const password2 = this.get('password2');
      const role = this.get('role');
      $.ajax({
        url: 'http://localhost:8000/rest-auth/registration/',
        method: 'POST',
        data: {
          username:email,
          first_name, last_name, email, password1, password2, role
        }
      }).done(data => {
        this.get('session').authenticate('authenticator:django', {
          username:email, email, password:password1
        }).then(success => {
          window.location.reload();
        });
      });
    }
  }
});

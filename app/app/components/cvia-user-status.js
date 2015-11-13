import Ember from 'ember';

export default Ember.Component.extend({
  tagName: 'div',
  classNames: ['right', 'item'],
  session: Ember.inject.service('session'),
  actions: {
    logout() {
      this.get('session').invalidate();
      localStorage.removeItem('ember_simple_auth:session');
      window.location.reload(true);
    }
  }
});

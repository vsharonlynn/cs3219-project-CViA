import Ember from 'ember';

export default Ember.Component.extend({
  tagName: 'div',
  classNames: ['card'],
  actions: {
    selectResume(resume) {
      this.sendAction('action', resume);
      return true;
    },
  }
});

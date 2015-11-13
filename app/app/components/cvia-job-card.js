import Ember from 'ember';

export default Ember.Component.extend({
  tagName: 'div',
  classNames: ['ui', 'card'],
  actions: {
    showResumeSelectModal() {
      this.$('.ui.modal').modal('show');
    }
  }
});

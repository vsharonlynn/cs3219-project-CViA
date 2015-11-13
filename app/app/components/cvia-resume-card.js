import Ember from 'ember';

export default Ember.Component.extend({
  tagName: 'div',
  classNames: ['card'],
  actions: {
    deleteResumeStart() {
      this.$('.dimmer').dimmer('show');
    },

    deleteResumeCancel() {
      this.$('.dimmer').dimmer('hide');
    },

    deleteResumeOk(id) {
      this.get('store').findRecord('resume', id)
        .then(resume => {
          this.$('.dimmer').dimmer('hide');
          this.$().slideUp('medium', () => {
            resume.destroyRecord();
          });
        });
    },
  }
});

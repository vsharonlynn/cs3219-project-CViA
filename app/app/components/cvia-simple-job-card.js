import Ember from 'ember';

export default Ember.Component.extend({
  tagName: 'div',
  classNames: ['card'],
  actions: {
    deleteJobStart() {
      this.$('.dimmer').dimmer('show');
    },

    deleteJobCancel() {
      this.$('.dimmer').dimmer('hide');
    },

    deleteJobOk(id) {
      this.get('store').findRecord('job', id)
        .then(job => {
          this.$('.dimmer').dimmer('hide');
          this.$().slideUp('medium', () => {
            job.destroyRecord();
          });
        });
    },
  }
});

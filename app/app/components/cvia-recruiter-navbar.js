import Ember from 'ember';

export default Ember.Component.extend({
  tagName: '',
  actions: {
    showCreateJobModal() {
      $('#upload-job-modal').modal('show');
    }
  }
});

import Ember from 'ember';
import $ from 'jquery';

export default Ember.Component.extend({
  tagName: '',
  actions: {
    showCreateCVModal() {
      $('#upload-cv-modal').modal('show');
    }
  }
});

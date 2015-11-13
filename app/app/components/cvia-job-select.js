import Ember from 'ember';

export default Ember.Component.extend({
  actions: {
    submitCV(resume) {
      const job = this.get('job');
      const submission = this.get('store').createRecord('submission', {
        job: this.get('job'),
        resume: resume
      });
      submission.save();
    }
  }
});

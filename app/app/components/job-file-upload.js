import Ember from 'ember';
import $ from 'jquery';
import EmberUploader from 'ember-uploader';

export default EmberUploader.FileField.extend({
  url: '',
  session: Ember.inject.service('session'),
  filesDidChange(files) {
    const uploadUrl = 'http://localhost:8000/api/uploads/';
    this.get('session').authorize('authorizer:django', (headerName, headerValue) => {
      const Uploader = EmberUploader.Uploader.extend({
        ajaxSettings() {
          var settings = this._super.apply(this, arguments);
          settings.headers = {
            [headerName]: [headerValue]
          };
          return settings;
        }
      });
      const uploader = Uploader.create({
        url: uploadUrl,
        paramName: 'datafile',
        type: 'POST'
      });
      if (!Ember.isEmpty(files)) {
        uploader.upload(files[0]).then(
          (data) => {
            const newJob = this.get('store').createRecord('job', {
              title: this.get('title') || "Untitled Job",
              description: this.get('description') || "No Description",
            });
            this.get('store').findRecord('upload', data.id).then(upload => {
              newJob.set('raw', upload);
              newJob.save().then((ok) => {
                files[0] = null;
                $('#upload-job-modal').modal('hide');
              }).catch((err) => {
                console.log(err);
              });
            }).catch(err => console.log(err));
          }
        ).catch((error) => {
          console.log(error);
          alert("Upload failed");
        })
      }
    });
  }
});

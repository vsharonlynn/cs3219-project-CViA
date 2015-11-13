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
            const newResume = this.get('store').createRecord('resume', {
              title: this.get('title') || "Untitled Resume"
            });
            this.get('store').findRecord('upload', data.id).then(upload => {
              newResume.set('raw', upload);
              newResume.save().then((ok) => {
                files[0] = null;
                $('#upload-cv-modal').modal('hide');
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

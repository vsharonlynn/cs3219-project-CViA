import DS from 'ember-data';

export default DS.Model.extend({
  datafile: DS.attr('string'),
  owner: DS.belongsTo('user'),
  url: (function(){
    const urls = this.get('datafile').split('/');
    return 'http://localhost:8000/files/' + urls[urls.length - 1];
  }).property('datafile'),
  created: DS.attr('string', {
    defaultValue() {
      return new Date();
    }
  })
});

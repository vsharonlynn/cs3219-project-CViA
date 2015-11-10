import DS from 'ember-data';

export default DS.Model.extend({
  title: DS.attr('string'),
  author: DS.belongsTo('user'),
  raw: DS.attr('string'),

  ago: Ember.computed('createdAt', function() {
    return moment(this.get('createdAt')).fromNow();
  }),

  url: Ember.computed('raw', function() {
    const rawUrl = this.get('raw');
    const split = rawUrl.split('/');
    return 'http://localhost:8000/files/' + split[split.length - 1];
  }),

  createdAt: DS.attr('string', {
    defaultValue() {
      return new Date();
    }
  })  
});

import DS from 'ember-data';

export default DS.Model.extend({
  job: DS.belongsTo('job'),
  resume: DS.belongsTo('resume'),
  score_1: DS.attr('number'),
  score_2: DS.attr('number'),
  score_3: DS.attr('number'),
  score_4: DS.attr('number'),
  max_score: DS.attr('number'),
  createdAt: DS.attr('string', {
    defaultValue() {
      return new Date();
    }
  })
});

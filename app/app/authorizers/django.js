import Base from 'ember-simple-auth/authorizers/base';
import { isEmpty } from 'ember';

export default Base.extend({
  authorize(data, block) {
    const accessToken = data['key'];
    if (!Ember.isEmpty(accessToken)) {
      block('Authorization', `Token ${accessToken}`);
    }
  }
});

import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils';
import UserChip from '@/components/UserChip.vue';

describe('UserChip.vue', () => {

  let wrapper;
  const author = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    affiliation: 'Example Inc.'
  };

  wrapper = mount(UserChip, {
    props: {
      author: author
    }
  });

  it('renders author name', () => {
    expect(wrapper.text()).toContain(author.name);
  });

  it('does not render email and affiliation if not provided', () => {
    const incompleteAuthor = { name: 'John Doe', email: null, affiliation: null };
    wrapper = mount(UserChip, {
      props: { author: incompleteAuthor }
    });
    expect(wrapper.text()).not.toContain('@'); // assuming email contains '@'
    expect(wrapper.text()).not.toContain('Inc.'); // assuming affiliation ends with 'Inc.'
  });

  it('shows popover when hover', async () => {
    await wrapper.trigger('mouseenter');
    expect(wrapper.find('.va-popover').exists()).toBe(true);
  });
});

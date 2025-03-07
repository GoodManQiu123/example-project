import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils';
import ErrorPage from '@/views/ErrorPage.vue';
import { setupRouter } from '../setup';

let router = setupRouter();

describe('ErrorPage', () => {

  it('renders correctly', () => {
    const wrapper = mount(ErrorPage);
    expect(wrapper.exists()).toBe(true);
  });

  it('renders error message from route query', async () => {
    await router.push({path: '/error', query: {msg: 'Invalid Request'}});
    await router.isReady();

    const wrapper = mount(ErrorPage);
    expect(wrapper.text()).toContain('Oops!');
    expect(wrapper.text()).toContain('Invalid Request');
  });

  it('render back button', () => {
    const wrapper = mount(ErrorPage);
    expect(wrapper.text()).toContain('Back');
  });
});

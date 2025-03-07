import { mount } from '@vue/test-utils'
import { describe, expect, it } from "vitest";
import SearchResult from "@/components/SearchResult.vue";

describe('SearchResult.vue', () => {
  let wrapper;

  const searchResults = [
    { articleId: 1, title: 'First Result', authors: [{authorId: 1, name: 'test'}] },
    { articleId: 2, title: 'Second Result', authors: [{authorId: 1, name: 'test'}] }
  ];

  wrapper = mount(SearchResult, {
    props: {
      modelValue: true,
      search: 'test',
      searchResults: searchResults
    }
  });

  it('renders correctly', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('does not render search results when there are none', () => {
    wrapper = mount(SearchResult, {
      props: {
        modelValue: true,
        search: 'test',
        searchResults: []
      }
    });
    const searchResults = wrapper.findAll('.va-list-item');
    expect(searchResults.length).toBe(0);
  });

  it('renders search results when there are some', () => {
    const searchResults = document.body.querySelectorAll('.va-list-item');
    expect(searchResults.length).toBe(2);
  });

  it('emits "update:modelValue" when the modal is closed', async () => {
    await wrapper.vm.handleClose();
    expect(wrapper.emitted('update:modelValue')).toBeTruthy();
    expect(wrapper.emitted('update:modelValue')[0]).toEqual([false]);
  });
});

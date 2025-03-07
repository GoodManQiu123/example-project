import { mount } from '@vue/test-utils'
import { describe, expect, it } from "vitest";
import PaperList from '@/components/PaperList.vue'

describe('PaperList.vue', () => {

  let wrapper;

  const originalPaper = {
    articleId: 1,
    title: 'Original Paper',
    authors: [{authorId: 1, name: 'test'}]
  };

  const papers = [
    {
      articleId: 1,
      title: 'First Paper',
      authors: [{authorId: 1, name: 'test'}]
    },
    {
      articleId: 2,
      title: 'Second Paper',
      authors: [{authorId: 1, name: 'test'}]
    }
  ]

  wrapper = mount(PaperList, {
    props: {
      papers: papers,
      originalPaper: originalPaper
    }
  });

  it('renders correctly', () => {
    expect(wrapper.exists()).toBe(true);
  })

  it('renders the original paper', () => {
    const originalPaper = wrapper.find('.va-list-item');
    expect(originalPaper.text()).toContain('Original Paper');
  })

  it('renders the list of papers', () => {
    const papers = wrapper.findAll('.va-list-item');
    expect(papers.length).toBe(2);
  })
})

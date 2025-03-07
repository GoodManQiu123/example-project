import { mount } from '@vue/test-utils'
import { describe, expect, it } from "vitest";
import DashboardCard from '@/components/DashboardCard.vue'
import { setupRouter } from "../setup.js";

const router = setupRouter();

describe('DashboardCard.vue', () => {
  it('renders correctly', () => {
    const wrapper = mount(DashboardCard, {})
    expect(wrapper.exists()).toBe(true)
  })

  it('props work correctly', () => {
    const wrapper = mount(DashboardCard, {
      props: {
        ready: 1,
        title: 'Test Title',
        section: 'Test Section',
        content: 'Test Content',
        link: '/test',
        paperId: 123,
      },
    })
    expect(wrapper.props().ready).toBe(1)
    expect(wrapper.props().title).toBe('Test Title')
    expect(wrapper.props().section).toBe('Test Section')
    expect(wrapper.props().content).toBe('Test Content')
    expect(wrapper.props().link).toBe('/test')
    expect(wrapper.props().paperId).toBe(123)
  })

  it('getReadyIcon and getReadyStripe work correctly', () => {
    const wrapper = mount(DashboardCard, {
      props: {
        ready: 1,
      },
    })
    expect(wrapper.vm.getReadyIcon()).toBe('check')
    expect(wrapper.vm.getReadyStripe()).toBe('success')
  })

  it('handleClick navigates correctly when no paper uploaded', async () => {
    const wrapper = mount(DashboardCard, {
      props: {
        link: '/topic/same-topic',
      },
    })
    // await the handleClick to ensure navigation is complete
    await wrapper.vm.handleClick('/topic/same-topic')
    // now perform the assertion
    expect(router.currentRoute.value.fullPath).toBe('/topic/same-topic')
  })

  it('handleClick navigates correctly when paper uploaded', async () => {
    const wrapper = mount(DashboardCard, {
      props: {
        link: '/topic/same-topic',
        paperId: 123,
      },
    })
    // await the handleClick to ensure navigation is complete
    await wrapper.vm.handleClick('/topic/same-topic')
    // now perform the assertion
    expect(router.currentRoute.value.fullPath).toBe('/topic/same-topic?paperId=123')
  })

})

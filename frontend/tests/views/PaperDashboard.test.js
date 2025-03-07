import { mount } from '@vue/test-utils'
import { describe, expect, it } from "vitest";
import PaperDashboard from "@/views/PaperDashboard.vue";

describe('PaperDashboard.vue', () => {
  let wrapper;

  wrapper = mount(PaperDashboard, {
    global: {
      stubs: {
        DashboardCard: true,
      },
    },
  });

  it('mounts successfully', () => {
    expect(wrapper).toBeTruthy();
  });

  it('updates "uploaded" state on file addition', async () => {
  });

  it('populates "paper" data after file upload', async () => {
    // Simulate file upload
    await wrapper.vm.onFileAdded();
    expect(wrapper.vm.paper).toEqual(expect.any(Object));
  });

  it('renders dashboard cards with correct "ready" states', async () => {
    const dashboardCards = wrapper.findAllComponents({ name: 'DashboardCard' });
    expect(dashboardCards).toHaveLength(6);
    expect(dashboardCards.at(0).props('ready')).toBe(-1);
  });
});

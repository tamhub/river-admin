<template>
    <div>
        <v-container v-if="initialized">
            <v-row>
                <v-col justify="between" align="between">
                    <h3 class="font-bold">
                        Workflow
                        <!-- <v-chip>{{ workflow.identifier }}</v-chip> -->
                    </h3>
                </v-col>
            </v-row>
            <div class="flex w-full">
                <v-flex xxs12 md3>
                    <v-container>


                        <div class="  rounded-[20px] gap-5 overflow-x-hidden flex flex-col w-full h-full">
                            <div class="flex flex-col w-full items-start justify-start gap-6 container flex-none">
                                <svg width="64" height="64" viewBox="0 0 64 64" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M57.522 45.864L56.5636 45.5785V45.5785L57.522 45.864ZM57.522 7.46644L56.5636 7.75191V7.75191L57.522 7.46644ZM25.682 7.46644L26.6404 7.75191H26.6404L25.682 7.46644ZM25.6304 21.5277L24.6304 21.526L24.6289 22.4392L25.5382 22.5235L25.6304 21.5277ZM37.2569 26.1332L36.2985 26.4187L36.2985 26.4187L37.2569 26.1332ZM37.3327 50.4717L36.3327 50.4729L36.3338 51.384L37.241 51.4675L37.3327 50.4717ZM56.601 45.3307C56.601 45.4102 56.5894 45.492 56.5636 45.5785L58.4804 46.1495C58.5591 45.8851 58.601 45.6112 58.601 45.3307H56.601ZM56.5636 7.75191C56.5528 7.71257 56.5391 7.65035 56.5352 7.62827C56.5331 7.61433 56.5299 7.59041 56.5288 7.58122C56.5267 7.56304 56.5258 7.54967 56.5256 7.54594C56.525 7.53719 56.5249 7.53388 56.5252 7.54056C56.5256 7.55214 56.5263 7.57453 56.527 7.61077C56.5285 7.68177 56.53 7.78806 56.5315 7.92938C56.5346 8.21107 56.5375 8.62094 56.5404 9.1419C56.5461 10.1833 56.5514 11.6624 56.5564 13.4342C56.5662 16.9774 56.5745 21.6875 56.5811 26.3982C56.5943 35.8198 56.601 45.2414 56.601 45.3307H58.601C58.601 45.24 58.5943 35.8172 58.5811 26.3954C58.5745 21.6845 58.5662 16.9733 58.5564 13.4286C58.5514 11.6565 58.5461 10.1751 58.5404 9.1309C58.5375 8.60909 58.5345 8.19495 58.5314 7.90782C58.5299 7.76474 58.5283 7.65043 58.5266 7.56919C58.5258 7.52931 58.5248 7.49268 58.5237 7.46289C58.5231 7.44888 58.5223 7.4293 58.5209 7.40877C58.5202 7.39914 58.5189 7.38101 58.5164 7.35919C58.5151 7.34817 58.5117 7.32271 58.5093 7.30753C58.5053 7.28418 58.4914 7.22099 58.4804 7.18098L56.5636 7.75191ZM41.602 3.66675C45.675 3.66675 49.3531 4.1845 52.0815 5.01287C53.4481 5.42778 54.5392 5.90947 55.3155 6.41671C56.1111 6.93654 56.4607 7.40639 56.5636 7.75191L58.4804 7.18098C58.1819 6.17903 57.3779 5.37518 56.4095 4.74242C55.4218 4.09707 54.1386 3.54727 52.6625 3.09912C49.7056 2.20137 45.825 1.66675 41.602 1.66675V3.66675ZM26.6404 7.75191C26.7433 7.40639 27.0929 6.93654 27.8885 6.41671C28.6648 5.90947 29.7559 5.42778 31.1225 5.01287C33.8509 4.1845 37.529 3.66675 41.602 3.66675V1.66675C37.379 1.66675 33.4984 2.20137 30.5415 3.09912C29.0654 3.54727 27.7822 4.09707 26.7945 4.74242C25.8261 5.37518 25.0221 6.17903 24.7236 7.18098L26.6404 7.75191ZM26.6304 21.5294C26.6368 17.7552 26.6443 14.2587 26.6529 11.6969C26.6572 10.4158 26.6618 9.3694 26.6666 8.63918C26.6691 8.27375 26.6715 7.9893 26.6741 7.79477C26.6753 7.69696 26.6766 7.62511 26.6777 7.57816C26.6783 7.55389 26.6788 7.5415 26.679 7.53747C26.6791 7.53458 26.6788 7.54156 26.6779 7.5536C26.6774 7.55913 26.6762 7.57401 26.6738 7.59366C26.6735 7.59532 26.6659 7.66636 26.6404 7.75191L24.7236 7.18098C24.6978 7.26766 24.6898 7.34061 24.6893 7.34494C24.6865 7.36728 24.6849 7.38561 24.6841 7.39536C24.6825 7.41585 24.6816 7.43433 24.6811 7.44599C24.6799 7.47103 24.679 7.49985 24.6783 7.52856C24.6769 7.5876 24.6755 7.66891 24.6742 7.76888C24.6716 7.9699 24.6691 8.25945 24.6667 8.62593C24.6618 9.35952 24.6572 10.4086 24.6529 11.6902C24.6443 14.2537 24.6368 17.7516 24.6304 21.526L26.6304 21.5294ZM25.5382 22.5235C28.6032 22.8074 31.2469 23.3909 33.1765 24.1491C34.1422 24.5285 34.8959 24.9388 35.4291 25.3523C35.9697 25.7714 36.2154 26.1397 36.2985 26.4187L38.2152 25.8477C37.9689 25.0208 37.3784 24.3329 36.6546 23.7717C35.9235 23.2048 34.9845 22.7106 33.9079 22.2876C31.7527 21.4408 28.9125 20.8275 25.7227 20.532L25.5382 22.5235ZM36.2985 26.4187C36.2786 26.3519 36.2706 26.2982 36.2688 26.2863C36.2656 26.2655 36.2638 26.2493 36.263 26.2415C36.2614 26.2255 36.2608 26.2147 36.2607 26.2139C36.2605 26.2109 36.2608 26.2149 36.2613 26.2301C36.2623 26.2589 36.2635 26.3053 36.2647 26.3716C36.2671 26.5027 36.2695 26.695 36.2718 26.9435C36.2765 27.4396 36.281 28.1499 36.2852 29.022C36.2936 30.7657 36.3009 33.1505 36.3073 35.7491C36.3199 40.9461 36.3284 46.9951 36.3327 50.4729L38.3327 50.4705C38.3284 46.9925 38.3199 40.9425 38.3073 35.7442C38.3009 33.1453 38.2936 30.7585 38.2851 29.0124C38.2809 28.1395 38.2765 27.4254 38.2717 26.9246C38.2694 26.6745 38.2669 26.4752 38.2643 26.3349C38.2631 26.2655 38.2617 26.2063 38.2601 26.1611C38.2594 26.1394 38.2584 26.1144 38.2569 26.0905C38.2562 26.0792 38.2549 26.06 38.2526 26.0377C38.2515 26.0267 38.2494 26.0079 38.2459 25.9849C38.2438 25.9709 38.2355 25.9156 38.2152 25.8477L36.2985 26.4187ZM41.602 49.6637C40.1534 49.6637 38.7523 49.5982 37.4244 49.4759L37.241 51.4675C38.6313 51.5955 40.0936 51.6637 41.602 51.6637V49.6637ZM56.5636 45.5785C56.4607 45.924 56.1111 46.3939 55.3155 46.9137C54.5392 47.421 53.4481 47.9027 52.0815 48.3176C49.3531 49.1459 45.675 49.6637 41.602 49.6637V51.6637C45.825 51.6637 49.7056 51.1291 52.6625 50.2313C54.1386 49.7832 55.4218 49.2334 56.4095 48.588C57.3779 47.9552 58.1819 47.1514 58.4804 46.1494L56.5636 45.5785Z"
                                        fill="#5E45FF" />
                                    <path
                                        d="M37.3335 53.3333C37.3335 53.5132 37.3067 53.6912 37.2545 53.8666C36.4517 56.5617 29.6301 59.9999 21.3335 59.9999C13.0369 59.9999 6.21526 56.5617 5.4125 53.8666C5.36025 53.6912 5.3335 53.5132 5.3335 53.3333C5.3335 53.1533 5.36025 26.3087 5.4125 26.1333C6.21526 23.4381 13.0369 21.3333 21.3335 21.3333C29.6301 21.3333 36.4517 23.4381 37.2545 26.1333C37.3067 26.3087 37.3335 53.1533 37.3335 53.3333Z"
                                        stroke="#5E45FF" stroke-width="2" />
                                    <path
                                        d="M37.3261 26.6667C37.3261 30.6667 30.168 33.3334 21.3335 33.3334C12.499 33.3334 5.34086 30.6667 5.3335 26.6667"
                                        stroke="#5E45FF" stroke-width="2" />
                                    <path
                                        d="M57.6001 8C56.7432 9.48148 50.168 12.6667 41.3335 12.6667C32.499 12.6667 26.6668 9.33333 25.3335 8"
                                        stroke="#5E45FF" stroke-width="2" />
                                    <path d="M57.3335 33.3333C56.0002 35.9999 46.6668 38.6666 37.3335 37.3333"
                                        stroke="#5E45FF" stroke-width="2" />
                                    <path d="M57.3335 21.3333C56.0002 23.9999 46.6668 26.6666 37.3335 25.3333"
                                        stroke="#5E45FF" stroke-width="2" />
                                    <path
                                        d="M37.3261 40C37.3335 42.6667 30.168 46.6667 21.3335 46.6667C12.499 46.6667 5.3335 42.6667 5.3335 40"
                                        stroke="#5E45FF" stroke-width="2" />
                                </svg>
                                <h2 style="color: #121722;" class="font-bold text-2xl">FMS Workflow</h2>
                                <p style="color: #121722;">The workflow of the exiting FMS aims to fund the translated
                                    applications through an
                                    expense approval cycle.</p>
                            </div>

                            <ul class="flex flex-col w-full gap-1">

                                <li>
                                    <router-link class="flex items-center gap-2 justify-start py-3"
                                        style="color: #121722;" :to="`/workflow/edit/rules/${workflow.id}/`">
                                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <g clip-path="url(#clip0_24_2784)">
                                                <path
                                                    d="M11.3335 2C11.5086 1.8249 11.7165 1.68601 11.9452 1.59125C12.174 1.49649 12.4192 1.44772 12.6668 1.44772C12.9145 1.44772 13.1597 1.49649 13.3884 1.59125C13.6172 1.68601 13.8251 1.8249 14.0002 2C14.1753 2.1751 14.3142 2.38297 14.4089 2.61174C14.5037 2.84051 14.5524 3.08571 14.5524 3.33333C14.5524 3.58096 14.5037 3.82615 14.4089 4.05493C14.3142 4.2837 14.1753 4.49157 14.0002 4.66667L5.00016 13.6667L1.3335 14.6667L2.3335 11L11.3335 2Z"
                                                    stroke="#A0A2A7" stroke-linecap="round" stroke-linejoin="round" />
                                            </g>
                                            <defs>
                                                <clipPath id="clip0_24_2784">
                                                    <rect width="16" height="16" fill="white" />
                                                </clipPath>
                                            </defs>
                                        </svg>

                                        Edit Transitions
                                    </router-link>
                                </li>
                                <li>
                                    <router-link class="flex items-center gap-2 justify-start py-3"
                                        style="color: #121722;" :to="`/workflow/edit/${workflow.id}/`">
                                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M13.7268 8.94L8.94683 13.72C8.823 13.844 8.67595 13.9423 8.51408 14.0094C8.35222 14.0765 8.17872 14.111 8.0035 14.111C7.82828 14.111 7.65477 14.0765 7.49291 14.0094C7.33105 13.9423 7.18399 13.844 7.06016 13.72L1.3335 8V1.33333H8.00016L13.7268 7.06C13.9752 7.30982 14.1146 7.64775 14.1146 8C14.1146 8.35225 13.9752 8.69018 13.7268 8.94V8.94Z"
                                                stroke="#A0A2A7" stroke-linecap="round" stroke-linejoin="round" />
                                            <path d="M4.6665 4.66667H4.67317" stroke="#A0A2A7" stroke-width="1.5"
                                                stroke-linecap="round" stroke-linejoin="round" />
                                        </svg>


                                        Add States
                                    </router-link>
                                </li>
                                <li>
                                    <router-link class="flex items-center gap-2 justify-start py-3"
                                        style="color: #121722;" :to="`/workflow-object/${workflow.id}/`">
                                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M9.33317 1.33333H3.99984C3.64622 1.33333 3.30708 1.47381 3.05703 1.72386C2.80698 1.97391 2.6665 2.31304 2.6665 2.66667V13.3333C2.6665 13.687 2.80698 14.0261 3.05703 14.2761C3.30708 14.5262 3.64622 14.6667 3.99984 14.6667H11.9998C12.3535 14.6667 12.6926 14.5262 12.9426 14.2761C13.1927 14.0261 13.3332 13.687 13.3332 13.3333V5.33333L9.33317 1.33333Z"
                                                stroke="#A0A2A7" stroke-linecap="round" stroke-linejoin="round" />
                                            <path d="M10.6668 11.3333H5.3335" stroke="#A0A2A7" stroke-linecap="round"
                                                stroke-linejoin="round" />
                                            <path d="M10.6668 8.66667H5.3335" stroke="#A0A2A7" stroke-linecap="round"
                                                stroke-linejoin="round" />
                                            <path d="M6.66683 6H6.00016H5.3335" stroke="#A0A2A7" stroke-linecap="round"
                                                stroke-linejoin="round" />
                                            <path d="M9.3335 1.33333V5.33333H13.3335" stroke="#A0A2A7"
                                                stroke-linecap="round" stroke-linejoin="round" />
                                        </svg>


                                        View Submissions
                                    </router-link>
                                </li>

                            </ul>

                        </div>
                    </v-container>
                </v-flex>
                <v-flex xxs12 md9>
                    <v-container>
                        <WorkflowIllustration :states="states" :transitions="transitions" :editable="true"
                            @on-transition-selected="on_transition_selected" @refetch="refetch" />
                    </v-container>
                </v-flex>

            </div>
        </v-container>

    </div>
</template>

<script>
import EmptyState from "@/components/EmptyState.vue";
import CreateApprovalForm from "@/components/CreateApprovalForm.vue";
import CreateTransitionHookForm from "@/components/CreateTransitionHookForm.vue";
import HookDetail from "@/components/HookDetail.vue";
import WorkflowIllustration from "@/components/WorkflowIllustration.vue";
import ApprovalList from "@/components/ApprovalList.vue";
import { emit_success } from "@/helpers/event_bus";
import http from "@/helpers/http";
import { Workflow, Approval, Transition, State, TransitionHook, ApprovalHook } from "@/models/models";

export default {
    name: "EditWorkflowRulesPage",
    components: {
        EmptyState,
        CreateApprovalForm,
        CreateTransitionHookForm,
        WorkflowIllustration,
        ApprovalList,
        HookDetail
    },
    props: ["readonly"],
    data: () => ({
        newApprovalDialog: false,
        newTransitionHookDialog: false,
        fab: false,
        workflow: null,
        initialized: false,
        selected_transition: null,
        states: [],
        transitions: [],
        alert_timeout: 2000,
        allowEditingHooks: false
    }),
    mounted() {
        this.refetch();
    },
    methods: {
        refetch() {
            var workflow_id = this.$route.params.id;
            this.workflow = http.get(`/workflow/get/${workflow_id}/`, response => {
                this.workflow = Workflow.of(response.data.id, response.data.content_type, response.data.initial_state, response.data.field_name);

                console.log(this.workflow);
                var state_fetcher = this.get_states(workflow_id).then(states => (this.states = states));
                var transitions_meta_fetcher = this.get_transition_metas(workflow_id).then(transitions => (this.transitions = transitions));

                Promise.all([state_fetcher, transitions_meta_fetcher]).then(() => {
                    var selected_transition_id = this.$route.query.selected_transition_id;
                    if (selected_transition_id) {
                        this.on_transition_selected(selected_transition_id);
                    }
                    this.initialized = true;
                });
            });
        },
        get_states(workflow_id) {
            return http.get(`/workflow/state/list/${workflow_id}/`, response => {
                return response.data.map(state => State.of(state.id, state.label).of_description(state.description));
            });
        },

        get_transition_metas(workflow_id) {
            var that = this;
            return http.get(`/workflow/transition-meta/list/${workflow_id}/`, response => {
                return Promise.all(
                    response.data.map(transition_meta => {
                        var transition = Transition.of(transition_meta.id, this.workflow, transition_meta.source_state, transition_meta.destination_state);

                        var transition_approval_metas_fetcher = that.get_transition_approval_metas(transition.id).then(transition_approval_metas => {
                            transition.approvals = transition_approval_metas;
                        });

                        var transition_hooks_fetcher = that.get_transition_hooks(transition.id).then(transition_hooks => {
                            transition.hooks = transition_hooks;
                        });

                        return Promise.all([transition_approval_metas_fetcher, transition_hooks_fetcher]).then(() => transition);
                    })
                );
            });
        },

        get_transition_hooks(transition_id) {
            return http.get(`/transition-meta/transition-hook/list/${transition_id}/`, response => {
                return response.data.map(transition_hook =>
                    TransitionHook.of(
                        transition_hook.id,
                        this.workflow,
                        transition_hook.callback_function,
                        transition_hook.transition_meta,
                        transition_hook.transition,
                        transition_hook.object_id,
                        false
                    )
                );
            });
        },

        get_transition_approval_metas(transition_id) {
            var that = this;
            return http.get(`/transition-meta/transition-approval-meta/list/${transition_id}/`, response => {
                return Promise.all(
                    response.data.map(transition_approval_meta => {
                        var approval = Approval.of(
                            transition_approval_meta.id,
                            this.workflow,
                            transition_approval_meta.transition,
                            transition_approval_meta.permissions,
                            transition_approval_meta.groups
                        );

                        return that
                            .get_transition_approval_hooks(approval.id)
                            .then(transition_approval_hooks => {
                                approval.hooks = transition_approval_hooks;
                            })
                            .then(() => approval);
                    })
                );
            });
        },
        get_transition_approval_hooks(transition_approval_meta_id) {
            return http.get(`/transition-approval-meta/approval-hook/list/${transition_approval_meta_id}/`, response => {
                return response.data.map(transition_approval_hook =>
                    ApprovalHook.of(
                        transition_approval_hook.id,
                        this.workflow,
                        transition_approval_hook.callback_function,
                        transition_approval_hook.transition_approval_meta,
                        transition_approval_hook.transition_approval,
                        transition_approval_hook.object_id,
                        false
                    )
                );
            });
        },

        on_approval_created(created_approval) {
            if (this.selected_transition) {
                var max_priority = this.selected_transition.approvals.reduce((max, approval) => Math.max(max, approval.priority), 0);
                created_approval.priority = max_priority + 1;
                http.post("/transition-approval-meta/create/", created_approval.to_create_request(), response => {
                    created_approval.id = response.data.id;
                    this.selected_transition.approvals.push(created_approval);
                    this._update_transition(this.selected_transition);
                    this.newApprovalDialog = false;
                    emit_success(`The transition approval meta is created`, this.alert_timeout);
                });
            }
        },
        on_approval_deleted(deleted_approval) {
            if (this.selected_transition) {
                http.delete(`/transition-approval-meta/delete/${deleted_approval.id}/`, response => {
                    this.selected_transition.approvals = this.selected_transition.approvals.filter(approval => approval.id != deleted_approval.id);
                    this._update_transition(this.selected_transition);
                    emit_success(`The transition approval meta is deleted`, this.alert_timeout);
                });
            }
        },
        on_approvals_order_change(newApprovals) {
            http
                .post(
                    `/transition-approval-meta/re-prioritize/`,
                    newApprovals.map(new_aproval => ({ transition_approval_meta_id: new_aproval.id, priority: new_aproval.priority }))
                )
                .then(response => {
                    this.selected_transition.approvals = newApprovals;
                    this._update_transition(this.selected_transition);
                    emit_success(`Re-prioritization has been applied`, this.alert_timeout);
                });
        },
        on_transition_hook_created(created_hook) {
            if (this.selected_transition && !this.selected_transition.hooks.find(hook => hook.id == created_hook.id)) {
                http.post("/transition-hook/create/", created_hook.to_create_request(), response => {
                    created_hook.id = response.data.id;
                    this.selected_transition.hooks.push(created_hook);
                    this._update_transition(this.selected_transition);
                    this.newTransitionHookDialog = false;
                    emit_success(`The transition hook is created`, this.alert_timeout);
                });
            }
        },
        on_transition_hook_deleted(deleted_hook) {
            if (this.selected_transition) {
                http.delete(`/transition-hook/delete/${deleted_hook.id}/`, response => {
                    this.selected_transition.hooks = this.selected_transition.hooks.filter(hook => hook.id != deleted_hook.id);
                    this._update_transition(this.selected_transition);
                    emit_success(`The transition hook is deleted`, this.alert_timeout);
                });
            }
        },
        on_approval_hook_created(created_hook) {
            if (this.selected_transition) {
                var approval = this.selected_transition.approvals.find(approval => approval.id == created_hook.transition_approval_meta_id);
                if (approval && !approval.hooks.find(hook => hook.id == created_hook.id)) {
                    http.post("/approval-hook/create/", created_hook.to_create_request(), response => {
                        created_hook.id = response.data.id;
                        approval.hooks.push(created_hook);
                        this._update_approval(this.selected_transition, approval);
                        this._update_transition(this.selected_transition);
                        emit_success(`The approval hook is created`, this.alert_timeout);
                    });
                }
            }
        },
        on_approval_hook_deleted(deleted_hook) {
            if (this.selected_transition) {
                var approval = this.selected_transition.approvals.find(approval => approval.id == deleted_hook.transition_approval_meta_id);
                if (approval) {
                    http.delete(`/approval-hook/delete/${deleted_hook.id}/`, response => {
                        approval.hooks = approval.hooks.filter(hook => hook.id != deleted_hook.id);
                        this._update_approval(this.selected_transition, approval);
                        this._update_transition(this.selected_transition);
                        emit_success(`The approval hook is deleted`, this.alert_timeout);
                    });
                }
            }
        },
        on_transition_selected(transition_id) {
            this.selected_transition = this.transitions.find(transition => transition.id == transition_id);

            this._update_query({
                selected_transition_id: JSON.stringify(transition_id)
            });
        },
        get_state_by(id) {
            return this.states.find(state => state.id == id);
        },
        _update_transition(transition) {
            // this._repriotise_approvals(transition);
            this.transitions = this.transitions.map(t => (t.id == transition.id ? transition : t));
        },
        _update_approval(transition, approval) {
            transition.approvals = transition.approvals.map(a => (a.id == approval.id ? approval : a));
        },
        _update_query(update) {
            var query = { ...this.$route.query, ...update };

            var that = this;
            if (Object.keys(query).some(queryKey => that.$route.query[queryKey] != query[queryKey])) {
                this.$router.push({ query });
            }
        },
        _repriotise_approvals(transition) {
            var that = this;
            transition.approvals = transition.approvals
                .sort((a1, a2) => a1.priority - a2.priority)
                .map((approval, index) => {
                    var newApproval = { ...approval, priority: index + 1 };
                    return newApproval;
                });
        }
    }
};
</script>



<style>
.fab_container {
    position: fixed;
    bottom: 45px;
    right: 30px;
    z-index: 10;
}

.v-chip__content {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    /* Prevents the text from wrapping */
    width: 100%;
}

.approval-shadow {
    box-shadow: -2px 7px 16px 0px #BFBFBF1A;

    box-shadow: -10px 27px 29px 0px #BFBFBF17;

    box-shadow: -21px 61px 39px 0px #BFBFBF0D;

    box-shadow: -38px 109px 46px 0px #BFBFBF03;

    box-shadow: -59px 170px 50px 0px #BFBFBF00;

}
</style>
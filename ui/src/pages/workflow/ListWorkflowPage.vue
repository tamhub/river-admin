<template>
  <v-container class="sm:px-4" v-if="initialized">
    <v-container v-if="items.length == 0">
      <v-flex>
        <v-alert type="success" class="transition-swing" transition="scale-transition" v-model="messageAlert"
          v-if="message">{{ message }}</v-alert>
      </v-flex>
      <v-row justify="center" align="center">
        <v-col justify="start" align="start">
          <h1 class="text-2xl font-bold">
            Workflows
          </h1>
        </v-col>
        <EmptyState class="mt-32">
          <template v-slot:customIcon>
            <svg class="mb-5" width="233" height="190" viewBox="0 0 233 190" fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <g opacity="0.4">
                <path
                  d="M228.74 130.671L216.028 175.163C214.636 180.033 213.938 182.464 212.518 184.272C211.264 185.867 209.612 187.114 207.733 187.881C205.606 188.75 203.072 188.75 198.009 188.75L174.71 188.75H38.8208H26.2249C17.7999 188.75 13.5758 188.75 10.7433 186.995C8.2612 185.457 6.44183 183.046 5.6449 180.237C5.47701 179.646 5.37975 179.025 5.34733 178.355C4.83416 177.588 4.36481 176.788 3.94265 175.96C1.39038 170.951 1.39038 164.398 1.39038 151.283V24.8334C1.39038 11.9007 11.8744 1.41675 24.8071 1.41675H67.8295C73.557 1.41675 76.4275 1.41675 79.1225 2.06375C81.5118 2.63738 83.7919 3.58589 85.8871 4.86979C88.2494 6.31746 90.2779 8.34592 94.3253 12.3933L106.765 24.8334H174.674C187.788 24.8334 194.341 24.8334 199.35 27.3857C203.756 29.6307 207.346 33.2104 209.591 37.6165C212.143 42.6256 212.143 49.1829 212.143 62.2975L212.143 106.792C219.634 106.798 223.534 106.894 226.204 108.548C228.686 110.085 230.501 112.495 231.298 115.304C232.208 118.511 231.056 122.565 228.74 130.671Z"
                  fill="#E9E9E9" />
                <path
                  d="M212.143 106.792C211.682 106.792 211.207 106.792 210.719 106.792H24.8103L8.21643 164.87L8.19242 164.951C6.31766 171.513 5.20467 175.409 5.34733 178.355M212.143 106.792C219.634 106.798 223.534 106.894 226.204 108.548C228.686 110.085 230.501 112.495 231.298 115.304C232.208 118.511 231.056 122.565 228.74 130.671L216.028 175.163C214.636 180.033 213.938 182.464 212.518 184.272C211.264 185.867 209.612 187.114 207.733 187.881C205.606 188.75 203.072 188.75 198.009 188.75L174.71 188.75H38.8208H26.2249C17.7999 188.75 13.5758 188.75 10.7433 186.995C8.2612 185.457 6.44183 183.046 5.6449 180.237C5.47701 179.646 5.37975 179.025 5.34733 178.355M212.143 106.792L212.143 62.2975C212.143 49.1829 212.143 42.6256 209.591 37.6165C207.346 33.2104 203.756 29.6307 199.35 27.3857C194.341 24.8334 187.788 24.8334 174.674 24.8334H106.765M5.34733 178.355C4.83416 177.588 4.36481 176.788 3.94265 175.96C1.39038 170.951 1.39038 164.398 1.39038 151.283V24.8334M1.39038 24.8334H106.765M1.39038 24.8334C1.39038 11.9007 11.8744 1.41675 24.8071 1.41675H67.8295C73.557 1.41675 76.4275 1.41675 79.1225 2.06375C81.5118 2.63738 83.7919 3.58589 85.8871 4.86979C88.2494 6.31746 90.2779 8.34592 94.3253 12.3933L106.765 24.8334"
                  stroke="#B8B9BD" stroke-linecap="round" stroke-linejoin="round" />
                <path fill-rule="evenodd" clip-rule="evenodd"
                  d="M109.567 116.528C110.392 116.602 111.001 117.33 110.927 118.156L107.437 157.095C112.565 158.229 116.31 162.7 116.529 167.946C123.68 168.239 130.705 165.864 136.223 161.254C141.741 156.644 145.327 150.153 146.311 143.064C140.705 141.808 136.762 136.561 137.289 130.684C137.862 124.29 143.511 119.57 149.905 120.144C156.3 120.717 161.019 126.365 160.446 132.76C159.917 138.659 155.069 143.132 149.301 143.34C148.242 151.219 144.273 158.438 138.146 163.556C132.02 168.675 124.21 171.297 116.269 170.937C115.039 176.577 109.774 180.552 103.875 180.023C97.4807 179.45 92.7615 173.801 93.3347 167.407C93.8625 161.518 98.6939 157.05 104.449 156.827L107.939 117.888C108.013 117.063 108.742 116.454 109.567 116.528ZM149.638 123.132C144.893 122.706 140.702 126.208 140.277 130.952C139.852 135.697 143.353 139.887 148.097 140.313C152.842 140.738 157.033 137.237 157.458 132.492C157.883 127.748 154.382 123.557 149.638 123.132ZM105.683 159.854C100.939 159.429 96.748 162.93 96.3227 167.674C95.8974 172.419 99.3988 176.61 104.143 177.035C108.888 177.46 113.079 173.959 113.504 169.215C113.929 164.47 110.428 160.279 105.683 159.854Z"
                  fill="#B8B9BD" />
              </g>
            </svg>
          </template>
          <template v-slot:content>
            <v-row class="w-full">
              <h3 class="pt-10 pb-6 text-center text-4xl font-normal w-full">

                You don’t have any workflows yet...
              </h3>
            </v-row>
            <v-row justify="center" align="center">
              <v-col>
                <v-btn theme="light" class="rounded-full px-8 py-6" color="primary" @click="goToCreateWorkflowPage">
                  <svg width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                      d="M8.50004 15.25C12.1819 15.25 15.1667 12.2653 15.1667 8.58335C15.1667 4.90146 12.1819 1.91669 8.50004 1.91669C4.81814 1.91669 1.83337 4.90146 1.83337 8.58335C1.83337 12.2653 4.81814 15.25 8.50004 15.25Z"
                      stroke="white" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M8.5 5.91669V11.25" stroke="white" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M5.83337 8.58337H11.1667" stroke="white" stroke-linecap="round" stroke-linejoin="round" />
                  </svg>
                  <span class="font-bold capitalize">

                    Create New
                  </span>
                </v-btn>
              </v-col>
            </v-row>
          </template>
        </EmptyState>
      </v-row>
    </v-container>
    <v-container class="sm:px-4" v-else>
      <v-flex>
        <v-alert type="success" class="transition-swing" transition="scale-transition" v-model="messageAlert"
          v-if="message">{{ message }}</v-alert>
      </v-flex>
      <v-row justify="center" align="center">
        <v-col justify="start" align="start">
          <h1 class="text-2xl font-bold">
            Workflows
          </h1>
        </v-col>
        <div class="" v-if="has_add_workflow_permission">
          <v-btn theme="light" class="rounded-full" color="primary" @click="goToCreateWorkflowPage">
            <svg width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M8.50004 15.25C12.1819 15.25 15.1667 12.2653 15.1667 8.58335C15.1667 4.90146 12.1819 1.91669 8.50004 1.91669C4.81814 1.91669 1.83337 4.90146 1.83337 8.58335C1.83337 12.2653 4.81814 15.25 8.50004 15.25Z"
                stroke="white" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M8.5 5.91669V11.25" stroke="white" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M5.83337 8.58337H11.1667" stroke="white" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <span class="font-bold capitalize">

              Create New
            </span>
          </v-btn>
        </div>
      </v-row>
      <div class="flex items-start justify-start gap-5">
        <div v-for="item in items" :key="item.id" class="w-[440px] h-[240px] bg-white rounded-2xl transition-all"
          :class="hover ? 'shadow-2xl' : 'shadow-xl'">
          <v-card-text class="card-text">
            <v-row class="fill-height">
              <!-- <v-col v-if="item.admin_name">
                      <v-row class="mt-5 mb-10" align="center" justify="center" v-if="item.admin_icon">
                        <v-icon color="primary" x-large>{{ item.admin_icon }}</v-icon>
                      </v-row>
                      <v-row class="mt-5 mb-10" align="center" justify="center">
                        <H5Max v-model="item.admin_name" max="16" />
                      </v-row>
                    </v-col> -->
              <v-col>
                <div class=" mb-10 w-full flex items-center justify-between">
                  <svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                      d="M57.522 45.864L56.5636 45.5785V45.5785L57.522 45.864ZM57.522 7.46644L56.5636 7.75191V7.75191L57.522 7.46644ZM25.682 7.46644L26.6404 7.75191H26.6404L25.682 7.46644ZM25.6304 21.5277L24.6304 21.526L24.6289 22.4392L25.5382 22.5235L25.6304 21.5277ZM37.2569 26.1332L36.2985 26.4187L36.2985 26.4187L37.2569 26.1332ZM37.3327 50.4717L36.3327 50.4729L36.3338 51.384L37.241 51.4675L37.3327 50.4717ZM56.601 45.3307C56.601 45.4102 56.5894 45.492 56.5636 45.5785L58.4804 46.1495C58.5591 45.8851 58.601 45.6112 58.601 45.3307H56.601ZM56.5636 7.75191C56.5528 7.71257 56.5391 7.65035 56.5352 7.62827C56.5331 7.61433 56.5299 7.59041 56.5288 7.58122C56.5267 7.56304 56.5258 7.54967 56.5256 7.54594C56.525 7.53719 56.5249 7.53388 56.5252 7.54056C56.5256 7.55214 56.5263 7.57453 56.527 7.61077C56.5285 7.68177 56.53 7.78806 56.5315 7.92938C56.5346 8.21107 56.5375 8.62094 56.5404 9.1419C56.5461 10.1833 56.5514 11.6624 56.5564 13.4342C56.5662 16.9774 56.5745 21.6875 56.5811 26.3982C56.5943 35.8198 56.601 45.2414 56.601 45.3307H58.601C58.601 45.24 58.5943 35.8172 58.5811 26.3954C58.5745 21.6845 58.5662 16.9733 58.5564 13.4286C58.5514 11.6565 58.5461 10.1751 58.5404 9.1309C58.5375 8.60909 58.5345 8.19495 58.5314 7.90782C58.5299 7.76474 58.5283 7.65043 58.5266 7.56919C58.5258 7.52931 58.5248 7.49268 58.5237 7.46289C58.5231 7.44888 58.5223 7.4293 58.5209 7.40877C58.5202 7.39914 58.5189 7.38101 58.5164 7.35919C58.5151 7.34817 58.5117 7.32271 58.5093 7.30753C58.5053 7.28418 58.4914 7.22099 58.4804 7.18098L56.5636 7.75191ZM41.602 3.66675C45.675 3.66675 49.3531 4.1845 52.0815 5.01287C53.4481 5.42778 54.5392 5.90947 55.3155 6.41671C56.1111 6.93654 56.4607 7.40639 56.5636 7.75191L58.4804 7.18098C58.1819 6.17903 57.3779 5.37518 56.4095 4.74242C55.4218 4.09707 54.1386 3.54727 52.6625 3.09912C49.7056 2.20137 45.825 1.66675 41.602 1.66675V3.66675ZM26.6404 7.75191C26.7433 7.40639 27.0929 6.93654 27.8885 6.41671C28.6648 5.90947 29.7559 5.42778 31.1225 5.01287C33.8509 4.1845 37.529 3.66675 41.602 3.66675V1.66675C37.379 1.66675 33.4984 2.20137 30.5415 3.09912C29.0654 3.54727 27.7822 4.09707 26.7945 4.74242C25.8261 5.37518 25.0221 6.17903 24.7236 7.18098L26.6404 7.75191ZM26.6304 21.5294C26.6368 17.7552 26.6443 14.2587 26.6529 11.6969C26.6572 10.4158 26.6618 9.3694 26.6666 8.63918C26.6691 8.27375 26.6715 7.9893 26.6741 7.79477C26.6753 7.69696 26.6766 7.62511 26.6777 7.57816C26.6783 7.55389 26.6788 7.5415 26.679 7.53747C26.6791 7.53458 26.6788 7.54156 26.6779 7.5536C26.6774 7.55913 26.6762 7.57401 26.6738 7.59366C26.6735 7.59532 26.6659 7.66636 26.6404 7.75191L24.7236 7.18098C24.6978 7.26766 24.6898 7.34061 24.6893 7.34494C24.6865 7.36728 24.6849 7.38561 24.6841 7.39536C24.6825 7.41585 24.6816 7.43433 24.6811 7.44599C24.6799 7.47103 24.679 7.49985 24.6783 7.52856C24.6769 7.5876 24.6755 7.66891 24.6742 7.76888C24.6716 7.9699 24.6691 8.25945 24.6667 8.62593C24.6618 9.35952 24.6572 10.4086 24.6529 11.6902C24.6443 14.2537 24.6368 17.7516 24.6304 21.526L26.6304 21.5294ZM25.5382 22.5235C28.6032 22.8074 31.2469 23.3909 33.1765 24.1491C34.1422 24.5285 34.8959 24.9388 35.4291 25.3523C35.9697 25.7714 36.2154 26.1397 36.2985 26.4187L38.2152 25.8477C37.9689 25.0208 37.3784 24.3329 36.6546 23.7717C35.9235 23.2048 34.9845 22.7106 33.9079 22.2876C31.7527 21.4408 28.9125 20.8275 25.7227 20.532L25.5382 22.5235ZM36.2985 26.4187C36.2786 26.3519 36.2706 26.2982 36.2688 26.2863C36.2656 26.2655 36.2638 26.2493 36.263 26.2415C36.2614 26.2255 36.2608 26.2147 36.2607 26.2139C36.2605 26.2109 36.2608 26.2149 36.2613 26.2301C36.2623 26.2589 36.2635 26.3053 36.2647 26.3716C36.2671 26.5027 36.2695 26.695 36.2718 26.9435C36.2765 27.4396 36.281 28.1499 36.2852 29.022C36.2936 30.7657 36.3009 33.1505 36.3073 35.7491C36.3199 40.9461 36.3284 46.9951 36.3327 50.4729L38.3327 50.4705C38.3284 46.9925 38.3199 40.9425 38.3073 35.7442C38.3009 33.1453 38.2936 30.7585 38.2851 29.0124C38.2809 28.1395 38.2765 27.4254 38.2717 26.9246C38.2694 26.6745 38.2669 26.4752 38.2643 26.3349C38.2631 26.2655 38.2617 26.2063 38.2601 26.1611C38.2594 26.1394 38.2584 26.1144 38.2569 26.0905C38.2562 26.0792 38.2549 26.06 38.2526 26.0377C38.2515 26.0267 38.2494 26.0079 38.2459 25.9849C38.2438 25.9709 38.2355 25.9156 38.2152 25.8477L36.2985 26.4187ZM41.602 49.6637C40.1534 49.6637 38.7523 49.5982 37.4244 49.4759L37.241 51.4675C38.6313 51.5955 40.0936 51.6637 41.602 51.6637V49.6637ZM56.5636 45.5785C56.4607 45.924 56.1111 46.3939 55.3155 46.9137C54.5392 47.421 53.4481 47.9027 52.0815 48.3176C49.3531 49.1459 45.675 49.6637 41.602 49.6637V51.6637C45.825 51.6637 49.7056 51.1291 52.6625 50.2313C54.1386 49.7832 55.4218 49.2334 56.4095 48.588C57.3779 47.9552 58.1819 47.1514 58.4804 46.1494L56.5636 45.5785Z"
                      fill="#BFB5FF" />
                    <path
                      d="M37.3335 53.3333C37.3335 53.5132 37.3067 53.6912 37.2545 53.8666C36.4517 56.5617 29.6301 59.9999 21.3335 59.9999C13.0369 59.9999 6.21526 56.5617 5.4125 53.8666C5.36025 53.6912 5.3335 53.5132 5.3335 53.3333C5.3335 53.1533 5.36025 26.3087 5.4125 26.1333C6.21526 23.4381 13.0369 21.3333 21.3335 21.3333C29.6301 21.3333 36.4517 23.4381 37.2545 26.1333C37.3067 26.3087 37.3335 53.1533 37.3335 53.3333Z"
                      stroke="#BFB5FF" stroke-width="2" />
                    <path
                      d="M37.3261 26.6667C37.3261 30.6667 30.168 33.3334 21.3335 33.3334C12.499 33.3334 5.34086 30.6667 5.3335 26.6667"
                      stroke="#BFB5FF" stroke-width="2" />
                    <path
                      d="M57.6001 8C56.7432 9.48148 50.168 12.6667 41.3335 12.6667C32.499 12.6667 26.6668 9.33333 25.3335 8"
                      stroke="#BFB5FF" stroke-width="2" />
                    <path d="M57.3335 33.3333C56.0002 35.9999 46.6668 38.6666 37.3335 37.3333" stroke="#BFB5FF"
                      stroke-width="2" />
                    <path d="M57.3335 21.3333C56.0002 23.9999 46.6668 26.6666 37.3335 25.3333" stroke="#BFB5FF"
                      stroke-width="2" />
                    <path
                      d="M37.3261 40C37.3335 42.6667 30.168 46.6667 21.3335 46.6667C12.499 46.6667 5.3335 42.6667 5.3335 40"
                      stroke="#BFB5FF" stroke-width="2" />
                  </svg>


                  <span>


                    <Dropdown>
                      <template v-slot:button="{ toggleDropdown }">
                        <button @click="toggleDropdown" class=" p-1 rounded-full text-xl flex items-center">
                          <svg width="32" height="32" viewBox="0 0 32 32" fill="none"
                            xmlns="http://www.w3.org/2000/svg">
                            <path
                              d="M25.3333 17.3333C26.0697 17.3333 26.6667 16.7364 26.6667 16C26.6667 15.2636 26.0697 14.6667 25.3333 14.6667C24.597 14.6667 24 15.2636 24 16C24 16.7364 24.597 17.3333 25.3333 17.3333Z"
                              fill="#121722" stroke="#121722" stroke-width="1.5" stroke-linecap="round"
                              stroke-linejoin="round" />
                            <path
                              d="M16 17.3333C16.7363 17.3333 17.3333 16.7364 17.3333 16C17.3333 15.2636 16.7363 14.6667 16 14.6667C15.2636 14.6667 14.6666 15.2636 14.6666 16C14.6666 16.7364 15.2636 17.3333 16 17.3333Z"
                              fill="#121722" stroke="#121722" stroke-width="1.5" stroke-linecap="round"
                              stroke-linejoin="round" />
                            <path
                              d="M6.66671 17.3333C7.40309 17.3333 8.00004 16.7364 8.00004 16C8.00004 15.2636 7.40309 14.6667 6.66671 14.6667C5.93033 14.6667 5.33337 15.2636 5.33337 16C5.33337 16.7364 5.93033 17.3333 6.66671 17.3333Z"
                              fill="#121722" stroke="#121722" stroke-width="1.5" stroke-linecap="round"
                              stroke-linejoin="round" />
                          </svg>

                        </button>
                      </template>

                      <template v-slot:items>

                        <button @click="goToViewWorkflowPage(item.id)"
                          class="block px-4 py-2 w-full text-left text-sm leading-5 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 transition duration-150 ease-in-out">View
                          Workflow</button>

                        <button @click="goToEditWorkflowPage(item.id)" :disabled="!has_change_workflow_permission"
                          class="block px-4 py-2 w-full text-left text-sm leading-5 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 transition duration-150 ease-in-out">Edit
                          Workflow</button>

                        <button @click="goToEditWorkflowRulePage(item.id)" :disabled="!has_change_workflow_permission"
                          class="block px-4 py-2 w-full text-left text-sm leading-5 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 transition duration-150 ease-in-out">View
                          Workflow Rules</button>

                        <button @click="showDeletingDialog(item.id)" :disabled="!has_delete_workflow_permission"
                          class="block px-4 py-2 w-full text-left  text-sm leading-5 !text-red-600 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 transition duration-150 ease-in-out">Delete
                        </button>
                      </template>
                    </Dropdown>
                  </span>
                </div>
                <v-row class="mb-10 container px-5" align="center" justify="start">
                  <H5Max class="font-semibold" v-model="item.content_type.app_label" max="16" />
                </v-row>
                <!-- <v-row align="center" justify="center">
                        <H5Max v-model="item.field_name" max="16" />
                      </v-row> -->
              </v-col>
            </v-row>
          </v-card-text>

          <v-card-actions>
            <div class="flex-grow-1"></div>
            <div class="ml-auto !mr-3 -translate-y-3">

              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn icon color="primary" v-on="on" @click="goToViewWorkflowPage(item.id)">
                    <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path
                        d="M16 29.3333C23.3638 29.3333 29.3333 23.3638 29.3333 16C29.3333 8.6362 23.3638 2.66666 16 2.66666C8.63616 2.66666 2.66663 8.6362 2.66663 16C2.66663 23.3638 8.63616 29.3333 16 29.3333Z"
                        stroke="#5E45FF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                      <path d="M16 21.3333L21.3333 16L16 10.6667" stroke="#5E45FF" stroke-width="1.5"
                        stroke-linecap="round" stroke-linejoin="round" />
                      <path d="M10.6666 16H21.3333" stroke="#5E45FF" stroke-width="1.5" stroke-linecap="round"
                        stroke-linejoin="round" />
                    </svg>

                  </v-btn>
                </template>
                <span>View Workflow</span>
              </v-tooltip>
            </div>

          </v-card-actions>
        </div>
      </div>

      <v-dialog v-if="this.deletingWorkflow" v-model="deleteDialog" max-width="50%">
        <v-card>
          <v-card-title class="headline">
            Delete workflow &nbsp;
            <v-chip color="primary">{{ deletingWorkflow.identifier }}</v-chip>&nbsp; ?
          </v-card-title>

          <v-card-text>Deleting the workflow will delete all transitions and approval meta data belongs to
            it.</v-card-text>

          <v-card-actions>
            <div class="flex-grow-1"></div>

            <v-btn large color="primary" @click="deleteDialog = false">Close</v-btn>

            <v-btn large color="warning" @click="deleteWorkflow()">Agree</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </v-container>
</template>

<script>
import http from "@/helpers/http";
import EmptyState from "@/components/EmptyState.vue";
import H5Max from "@/components/H5Max.vue";
import { emit_success } from "@/helpers/event_bus";
import { auth, WORKFLOW } from "@/helpers/auth";
import { Workflow } from "@/models/models";
import Dropdown from "@/components/primatives/Dropdown.vue";
export default {
  name: "ListWorkflowPage",
  components: {
    EmptyState,
    H5Max,
    Dropdown
  },
  computed: {
    deletingWorkflowDialogTitle() {
      return `Delete workflow ${this.deletingWorkflow.identifier}?`;
    }
  },
  mounted() {
    this.fetchWorkflows();
    this.message = this.$route.query.message;
    if (this.$route.query.message) {
      this.setAlertMessage(this.$route.query.message);
    }
  },
  data: () => ({
    initialized: false,
    messageAlert: true,
    message: null,
    deletingWorkflow: null,
    deleteDialog: false,
    has_add_workflow_permission: false,
    has_delete_workflow_permission: false,
    has_change_workflow_permission: false,
    items: []
  }),
  methods: {
    setAlertMessage(message) {
      this.message = message;
      this.messageAlert = true;
      var that = this;
      setTimeout(() => (that.messageAlert = false), 3000);
    },
    fetchWorkflows() {
      var workflow_fetcher = http.get("/workflow/list/", response => {
        this.items = response.data.map(workflow => {
          var workflow_model = Workflow.of(workflow.id, workflow.content_type, workflow.initial_state, workflow.field_name);
          workflow_model.admin_name = workflow.admin_name;
          workflow_model.admin_icon = workflow.admin_icon;
          return workflow_model;
        });
      });

      var add_workflow_permission_checker = auth.has_add_permission(WORKFLOW, answer => {
        this.has_add_workflow_permission = answer;
      });

      var change_workflow_permission_checker = auth.has_change_permission(WORKFLOW, answer => {
        this.has_change_workflow_permission = answer;
      });

      var delete_workflow_permission_checker = auth.has_delete_permission(WORKFLOW, answer => {
        this.has_delete_workflow_permission = answer;
      });

      Promise.all([workflow_fetcher, add_workflow_permission_checker, change_workflow_permission_checker, delete_workflow_permission_checker]).then(
        () => (this.initialized = true)
      );
    },
    goToCreateWorkflowPage() {
      this.$router.push({ name: "create-workflow" });
    },
    goToViewWorkflowPage(workflowId) {
      this.$router.push({
        name: "view-workflow",
        params: { id: workflowId }
      });
    },
    goToEditWorkflowPage(workflowId) {
      this.$router.push({
        name: "edit-workflow",
        params: { id: workflowId }
      });
    },

    goToEditWorkflowRulePage(workflowId) {
      this.$router.push({
        name: "edit-workflow-rules",
        params: { id: workflowId }
      });
    },

    showDeletingDialog(workflow) {
      this.deletingWorkflow = workflow;
      this.deleteDialog = true;
    },
    deleteWorkflow() {
      if (this.deletingWorkflow) {
        http.delete(`/workflow/delete/${this.deletingWorkflow.id}/`, () => {
          this.fetchWorkflows();
          this.deleteDialog = false;
          emit_success(`Workflow ${this.deletingWorkflow.identifier} is deleted.`);
        });
      }
    }
  }
};
</script>


<style>
.fab_container {
  position: fixed;
  bottom: 45px;
  right: 30px;
}

.card-text {
  height: 80%;
  font-size: 30px;
}
</style>
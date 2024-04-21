<template>
    <div :style="{ width: width + 'px', height: height + 'px', color: color }">
        <component :is="svgComponent" :width="width" :height="height" :viewBox="`0 0 ${width} ${height}`" />
    </div>
</template>

<script>
// Import your SVG files
import git from '@/assets/icons/git.svg';
import tag from '@/assets/icons/tag.svg';
import zap from '@/assets/icons/zap.svg';
import db from '@/assets/icons/db.svg';
import list from '@/assets/icons/list.svg';

export default {
    name: 'Icon',
    props: {
        name: {
            type: String,
            required: true
        },
        width: {
            type: [String, Number],
            default: '32' // Ensure default is a string to match SVG attributes
        },
        height: {
            type: [String, Number],
            default: '32' // Ensure default is a string to match SVG attributes
        },
        color: {
            type: String,
            default: 'currentColor'
        }
    },
    computed: {
        svgComponent() {
            const icons = {
                git,
                tag,
                zap,
                db,
                list
            };
            return icons[this.name] || null;
        }
    }
}
</script>
import Mirador from 'mirador/dist/es/src/index';

const config = {
    id: 'demo',
    windows: [{manifestId: '../manifests/nla.obj-224441858-v3-manifest.json'}, {manifestId: '../manifests/nla.obj-224441684-v3-manifest.json'}],
    workspace: {
        type: "elastic"
    }
};

Mirador.viewer(config);
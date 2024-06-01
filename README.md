# Mirador on GH Pages

This repository deploys a basic installation of Mirador 3 on GitHub Pages.

## Intended use case

I had in mind a researcher who wants to create their own customised IIIF workspace to compare images or manuscripts without installing any software or fiddling about on the command line.

## Using this template

1. Click on the green **Use this template** button and select 'Create a new repository'
2. Give your new repository a name using the 'Repository name' field.
3. Click on the **Create repository** button

After a few seconds your new repository will be generated. The 'Publish website' action will run automatically to build your Mirador site. Look under the 'Actions' tab to view its progress. Once it's finished (you'll see a green tick), you have to configure GH Pages:

1. Click on the repository's 'Settings' tab.
2. Select 'Pages' from the left-hand menu.
3. Under 'Build and deployment':
  - set 'Source' to 'Deploy from a branch'
  - set 'Branch' to 'gh-pages'
  - click **Save**

Another action will now run to deploy your Mirador site to GH Pages. Once again you can check its status under the 'Actions' tab. When it's finished you'll be able to access your Mirador installation at: `https://[your GitHub user name].github.io/[your repository name]/. You can find the url by clicking on 'Deployments' from your repository's home page.

Any changes you make to the repository from now on will be automatically deployed to GH Pages.

## Adding default manifests

You can set default manifests by either uploading local manifests to the repository, or by adding manifest urls to the config file.

### Local manifests

If you have local manifests that you want to open by default in your Mirador workspace, all you need to do is upload them to the repository.

1. From your repository's home page click on the `manifests` folder to open it.
2. Click on the **Add files** button, then select 'Upload files'.
3. Select the manifests you want to upload.
4. Once the file has loaded, click on the green **Commit changes** button.

Uploading manifests automatically triggers the deploy actions. As part of the deployment, a little python script checks the `manifests` directory and adds the names of any files it finds to the Mirador configuration.

Once the actions have run, reload your Mirador workspace to see the manifests.

### Manifest urls

You can also add default manifest urls by directly editing the Mirador configuration. 

1. From your repository's home page click on the `src` folder to open it.
2. Click on the `index.js` file to view its contents.
3. Click on the pencil icon to edit the file.
4. Look for the line `windows: [],`.
5. Insert the urls into the `windows` array, for example:  `windows: [{manifestId: 'https://purl.stanford.edu/sn904cj3429/iiif/manifest'}]`
6. Click on the green **Commit changes** button.

A new version of your Mirador workspace will be automatically built and deployed.

## Mirador versions and plugins

This repository uses Mirador 3 which is nearing the end of its lifespan. Mirador 4 is in alpha release. Once it's ready I'll create a new Mirador 4 template.

The [Mirador Image Tools](https://github.com/ProjectMirador/mirador-image-tools) plugin is installed by default, though the image tools aren't displayed in the workspace. To display them click on the window's options icon and select 'Show image tools'.

I've also included the [Mirador Annotations](https://github.com/ProjectMirador/mirador-annotations) plugin as part of the package, but haven't initialised it in the Mirador config. Uncomment the annotations-related lines in the Mirador config to enable annotations using your browser's local storage.

## Credits

This repository was created by [Tim Sherratt](https://timsherratt.au), based on the [Mirador Integration](https://github.com/ProjectMirador/mirador-integration) example repository.



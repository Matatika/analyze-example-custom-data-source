# analyze-example-custom-data-source
Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets used in our [Getting Started Tutorial - Adding a Custom Data Source](https://www.matatika.com/docs/getting-started/adding-a-custom-data-source)

## Please Note

This analyze file bundle, and its related tap, are just for use in our [Getting Started Tutorial - Adding a Custom Data Source](https://www.matatika.com/docs/getting-started/adding-a-custom-data-source).

This custom data source is just tap-spreadsheets-anywhere, (which we already support by default in the Matatika platform), renamed and with an analyze file bundle so that following the getting started tutorial gets you visible results in your workspace.

---

Files:
- [`analyze/datasets/tap-example-custom-data-source`](./bundle/analyze/datasets/tap-example-custom-data-source) (directory)

To add [tap-example-custom-data-source](https://github.com/Matatika/tap-example-custom-data-source) and its related plugins to your Matatika workspace:
```yaml
extractors:
  - name: tap-example-custom-data-source
    namespace: tap_example_custom_data_source
    pip_url: git+https://github.com/ets/tap-spreadsheets-anywhere.git
    capabilities:
      - catalog
      - discover
      - state
    settings:
      - name: tables
        kind: array
files:
  - name: analyze-example-custom-data-source
    namespace: tap_example_custom_data_source
    update:
      analyze/datasets/tap-example-custom-data-source: true
    pip_url: git+https://github.com/Matatika/analyze-example-custom-data-source.git
```

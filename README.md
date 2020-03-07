# timezone
timezone Rest Api endpoint

### Usage

#### Build:

```bash
docker build -f timezone.Dockerfile .
```

#### Run:

```bash
docker run -it --rm -p 8080:5000 <latest_hash>
```


### Validation:
* Empty values for latitude and longtitude.
* No timeouts defined.

### Notes:
Running under non-root user.

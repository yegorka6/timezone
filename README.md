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

### Usage:
```bash
http://localhost:8080/endpoint?lat=11.56&long=45.55
```

### Validation:
* Empty values for latitude and longtitude.
* No timeouts defined.

### Notes:
Running under non-root user.

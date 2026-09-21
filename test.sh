for v in 3.10 3.11 3.12 3.13 3.14; do
    echo "=== Python $v ==="
    uv run --python $v pytest || exit 1
done

rm uv.lock
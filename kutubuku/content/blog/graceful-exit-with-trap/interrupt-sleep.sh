trap "echo 'Interrupted! Cleaning up...'; exit" SIGINT

while true; do
  echo "Running..."
  sleep 1
done

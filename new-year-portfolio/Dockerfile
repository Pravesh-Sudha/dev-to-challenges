# Use the official lightweight Nginx image
FROM nginx:alpine

# Copy the static website files to the Nginx html directory
COPY . /usr/share/nginx/html

# Expose port 8080 (Cloud Run default)
EXPOSE 8080

# Configure Nginx to listen on port 8080
# We overwrite the default conf to listen on 8080 instead of 80 to match Cloud Run default expectations easily, 
# though Cloud Run usually injects PORT env var, standard nginx image listens on 80.
# A simple sed replacement works well here.
RUN sed -i 's/listen       80;/listen       8080;/' /etc/nginx/conf.d/default.conf

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

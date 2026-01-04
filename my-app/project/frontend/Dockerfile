FROM nginx:alpine

# Copy static HTML
COPY index.html /usr/share/nginx/html/index.html

# Copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose HTTP port
EXPOSE 80

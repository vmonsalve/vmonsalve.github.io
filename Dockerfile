FROM ruby:3.1-alpine

RUN apk add --no-cache \
    build-base \
    curl \
    nodejs \
    npm \
    linux-headers \
    libffi-dev

RUN npm install -g yarn

WORKDIR /site

COPY Gemfile Gemfile.lock ./

RUN bundle install

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
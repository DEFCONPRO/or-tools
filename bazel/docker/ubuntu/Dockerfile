# Create a virtual environment with all tools installed
# ref: https://hub.docker.com/_/ubuntu
FROM ubuntu:rolling AS env
# Install system build dependencies
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install system build dependencies
RUN apt-get update -qq \
&& apt-get install -yq git wget curl libssl-dev build-essential \
&& apt-get install -yq python3-dev python3-pip \
&& apt-get install -yq default-jdk \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Install Bazel
RUN curl https://bazel.build/bazel-release.pub.gpg | apt-key add -
RUN echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
RUN apt-get update -qq \
&& apt-get install -yq bazel \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

FROM env AS devel
WORKDIR /home/project
COPY . .

FROM devel AS build
RUN bazel version
RUN bazel build \
 -c opt \
 --action_env=BAZEL_CXXOPTS="-std=c++17" \
 --subcommands=true \
 ortools/... examples/...

FROM build AS test
RUN bazel test \
 -c opt \
 --action_env=BAZEL_CXXOPTS="-std=c++17" \
 --test_output=errors \
 ortools/... examples/...

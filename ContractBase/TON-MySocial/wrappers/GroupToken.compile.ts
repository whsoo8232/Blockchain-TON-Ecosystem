import { CompilerConfig } from '@ton/blueprint';

export const compile: CompilerConfig = {
    lang: 'tact',
    target: 'contracts/group_token.tact',
    options: {
        debug: true,
    },
};
